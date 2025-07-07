from NewsAggregationSystem.server.database import db_query
from datetime import datetime
from NewsAggregationSystem.server.utilities.logger import logger


class ArticleRepo:
    def insert_article(self, article):
        published_at = article.get("published_at")
        if published_at:
            dt = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_published_at = dt.strftime("%Y-%m-%d %H:%M:%S")
        else:
            logger.warning("Article missing published_at, using current UTC time.")
            formatted_published_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(
            f"Inserting article: {article.get('title', 'No Title')} from source: {article.get('source', 'Unknown')}")
        query = '''INSERT INTO article (title,
                    description,
                    content,
                    source,
                    url,
                    published_at,
                    server_id) VALUES (%s, %s, %s, %s,%s, %s, %s)'''
        db_query(query, (article['title'],article['description'],article['content'],article['source'],article['url'],formatted_published_at,article['server_id']))

    def find_articles(self):
        query = '''Select * from article'''
        return db_query(query, ())

    def find_article_by_id(self, article_id):

        if isinstance(article_id, tuple):
            article_id = article_id[0]
        
        query = """
            SELECT a.* FROM article a
            WHERE a.article_id = %s AND
            a.is_hidden = FALSE
        """
        return db_query(query, (article_id,))

    def find_latest_article(self):
        query = '''Select * from article order by article_id desc limit 1'''
        return db_query(query, ())[0]

    def fetch_articles_by_user_preference(self, base_filter, category_filter, sort_by_filter, params):

        if category_filter:
            last_query = f"""
                    SELECT DISTINCT a.* FROM article a
                    JOIN category_article_mapping cam ON a.article_id = cam.article_id
                    JOIN category c ON cam.category_id = c.category_id
                    WHERE  {base_filter} {category_filter}{sort_by_filter}
                """
        else:
            last_query = f"""
                    SELECT DISTINCT a.* FROM article a
                    WHERE {base_filter} {sort_by_filter}
                """


        query = f"""    
                        SELECT DISTINCT a.* FROM category_article_mapping cam
                        JOIN keyword_article_mapping kam ON cam.article_id = kam.article_id
                        JOIN notification_setting ns 
                        ON ns.category_id = cam.category_id AND ns.keyword_id = kam.keyword_id
                        JOIN article a ON a.article_id = cam.article_id
                        WHERE {base_filter} AND ns.user_id = %s
                       UNION
                       (
                            SELECT DISTINCT a.* FROM article a
                            JOIN category_article_mapping cam ON a.article_id = cam.article_id
                            JOIN notification_setting ns ON cam.category_id = ns.category_id
                            WHERE {base_filter} AND ns.user_id = %s                
                        )
                       UNION
                        (
                            SELECT DISTINCT a.* FROM article a
                            JOIN keyword_article_mapping kam ON a.article_id = kam.article_id
                            JOIN notification_setting ns ON kam.keyword_id = ns.keyword_id
                            WHERE {base_filter} AND ns.user_id = %s                
                        )
                       UNION
                       (
                           SELECT DISTINCT a.* FROM article a
                           JOIN article_reaction ar ON a.article_id = ar.article_id
                           WHERE  {base_filter} AND ar.user_id = %s 
                       )
                       UNION
                       (
                           SELECT DISTINCT a.* FROM article a
                           JOIN saved_article sa ON a.article_id = sa.article_id
                           WHERE  {base_filter} AND sa.user_id = %s  
                       )
                       UNION
                       (
                           SELECT DISTINCT a.* FROM article a
                           JOIN read_article_history rah ON a.article_id = rah.article_id
                           WHERE {base_filter} AND rah.user_id = %s  
                       )
                       UNION
                       (
                            {last_query}
                        )
                    """
        return db_query(query, tuple(params))

    def fetch_articles_by_today(self, user_id):
        base_filter = "a.is_hidden = 0 AND DATE(a.published_at) = CURDATE()"
        category_filter = ""
        sort_by_filter = ""
        params = [user_id, user_id, user_id, user_id, user_id, user_id]

        return self.fetch_articles_by_user_preference(base_filter, category_filter, sort_by_filter, params)


    def fetch_articles_by_date_range(self, user_id, start_date, end_date, category):
        category = category.strip().lower()
        base_filter = "a.is_hidden = 0 AND DATE(a.published_at) BETWEEN %s AND %s"
        category_filter = ""
        sort_by_filter = ""
        params = [start_date, end_date, user_id, start_date, end_date, user_id, start_date, end_date, user_id,
                  start_date, end_date, user_id, start_date, end_date, user_id, start_date, end_date, user_id, start_date, end_date]

        if category != "all" and category.strip() != "":
            category_filter = "AND category_name = %s"
            params.append(category)

        return self.fetch_articles_by_user_preference(base_filter, category_filter, sort_by_filter, params)

    def search_articles(self, start_date, end_date, keyword, sort_by, user_id):
        keyword = keyword.strip().lower()
        keyword_like = f"%{keyword}%"
        category_filter = ""
        sort_by_filter = "order by likes DESC" if sort_by == "likes" else "order by dislikes DESC"
        base_filter = "a.is_hidden = 0 AND DATE(a.published_at) BETWEEN %s AND %s AND (a.title LIKE %s OR a.description LIKE %s OR a.content LIKE %s)"
        params = [start_date, end_date, keyword_like, keyword_like, keyword_like, user_id, start_date, end_date, keyword_like, keyword_like, keyword_like, user_id, start_date, end_date, keyword_like, keyword_like, keyword_like, user_id,
                  start_date, end_date, keyword_like, keyword_like, keyword_like, user_id, start_date, end_date, keyword_like, keyword_like, keyword_like, user_id, start_date, end_date, keyword_like, keyword_like, keyword_like, user_id, start_date, end_date, keyword_like, keyword_like, keyword_like]

        return self.fetch_articles_by_user_preference(base_filter, category_filter, sort_by_filter, params)

    def save_article(self, user_id, article_id):
        query = """
            INSERT INTO saved_article (user_id, article_id)
            VALUES (%s, %s)
        """
        return db_query(query, (user_id, article_id))

    def find_save_article(self, user_id, article_id):
        query = '''Select * from saved_article where user_id = %s and article_id = %s '''
        return db_query(query, (user_id, article_id))

    def get_saved_articles(self, user_id):
        query = """
            SELECT a.* FROM article a
            JOIN saved_article usa ON a.article_id = usa.article_id
            WHERE usa.user_id = %s and a.is_hidden = FALSE
        """
        return db_query(query, (user_id,))

    def get_reacted_articles(self, user_id):
        query = """
            SELECT a.* FROM article a
            JOIN article_reaction ar ON a.article_id = ar.article_id
            WHERE ar.user_id = %s and a.is_hidden = FALSE
        """
        return db_query(query, (user_id,))

    def delete_saved_article(self, user_id, article_id):
        query = """
               DELETE FROM saved_article
               WHERE user_id = %s AND article_id = %s
           """
        return db_query(query, (user_id, article_id))

    def search_articles_with_keyword(self, keyword):
        query = """
                  SELECT * FROM article
                  WHERE title LIKE %s OR description LIKE %s OR content LIKE %s 
              """
        like_pattern = f"%{keyword}%"
        return db_query(query, (like_pattern, like_pattern, like_pattern))


    def set_article_hidden(self, article_id: int, hidden: bool):
        query = "UPDATE article SET is_hidden = %s WHERE article_id = %s"
        return db_query(query, (hidden, article_id))

    def set_articles_hidden_by_category(self, category_id: str):
            query = """
                UPDATE article
                SET is_hidden = TRUE
                WHERE article_id IN (
                    SELECT article_id FROM category_article_mapping WHERE category_id = %s
                )
            """
            return db_query(query, (category_id,))

    def update_likes(self):
        query = """
        UPDATE article a
        LEFT JOIN (
            SELECT
                ar.article_id,
                SUM(CASE WHEN ar.is_like = TRUE THEN 1 ELSE 0 END) AS like_count
            FROM article_reaction ar
            GROUP BY ar.article_id
        ) AS react_summary ON a.article_id = react_summary.article_id
        SET
            a.likes = IFNULL(react_summary.like_count, 0);
        """
        db_query(query)

    def update_dislikes(self):
        query = """
        UPDATE article a
        LEFT JOIN (
            SELECT
                ar.article_id,
                SUM(CASE WHEN ar.is_dislike = TRUE THEN 1 ELSE 0 END) AS dislike_count
            FROM article_reaction ar
            GROUP BY ar.article_id
        ) AS react_summary ON a.article_id = react_summary.article_id
        SET
            a.dislikes = IFNULL(react_summary.dislike_count, 0);
        """
        db_query(query)


    def update_latest_status(self, article_id):
        query = "UPDATE article SET is_latest = 0 WHERE article_id = %s"
        return db_query(query, (article_id,))

    def get_latest_status(self, article_id):
        query = "SELECT is_latest from article WHERE article_id = %s"
        return db_query(query, (article_id,))