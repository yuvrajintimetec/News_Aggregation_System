from NewsAggregationSystem.server.database import db_query
from datetime import datetime



class ArticleRepo:
    def insert_article(self, article):
        published_at = article.get("published_at")
        if published_at:
            dt = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_published_at = dt.strftime("%Y-%m-%d %H:%M:%S")
        else:
            formatted_published_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
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
        query = '''Select * from article where article_id = %s'''
        return db_query(query, (article_id,))

    def find_latest_article(self):
        query = '''Select * from article order by article_id desc limit 1'''
        return db_query(query, ())[0]

    def fetch_articles_by_date(self, user_id):
        query = """
            SELECT * FROM article
            WHERE DATE(published_at) = CURDATE() and is_hidden = FALSE
        """
        return db_query(query)

    def fetch_articles_by_date_range(self, user_id, start_date, end_date, category):
        if category.lower() == "all":
            query = """
                SELECT * FROM article
                WHERE DATE(published_at) BETWEEN %s AND %s and is_hidden = FALSE
            """
            return db_query(query, (start_date, end_date))
        else:
            query = """
                SELECT a.* FROM article a
                JOIN category_article_mapping cam ON a.article_id = cam.article_id
                JOIN category c ON cam.category_id = c.category_id
                WHERE DATE(a.published_at) BETWEEN %s AND %s AND c.category_name = %s and a.is_hidden = FALSE
            """
            return db_query(query, (start_date, end_date, category))

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

    def delete_saved_article(self, user_id, article_id):
        query = """
               DELETE FROM saved_article
               WHERE user_id = %s AND article_id = %s
           """
        return db_query(query, (user_id, article_id))

    def search_articles(self,start_date, end_date, keyword, sort_by):
        sort_column = "like_count DESC" if sort_by == "likes" else "dislike_count DESC"

        query = f"""
                SELECT 
                    a.*,
                    COALESCE(SUM(CASE WHEN ar.is_like = TRUE THEN 1 ELSE 0 END), 0) AS like_count,
                    COALESCE(SUM(CASE WHEN ar.is_like = FALSE THEN 1 ELSE 0 END), 0) AS dislike_count
                FROM article a
                LEFT JOIN article_reaction ar ON a.article_id = ar.article_id
                WHERE a.published_at BETWEEN %s AND %s
                  AND (a.title LIKE %s OR a.description LIKE %s OR a.content LIKE %s) and a.is_hidden = FALSE
                GROUP BY a.article_id
                ORDER BY {sort_column}
            """
        keyword_like = f"%{keyword}%"
        return db_query(query, (start_date, end_date, keyword_like, keyword_like, keyword_like))


    def search_articles_with_keyword(self, keyword):
        query = """
                  SELECT * FROM article
                  WHERE title LIKE %s OR description LIKE %s OR content LIKE %s 
              """
        like_pattern = f"%{keyword}%"
        return db_query(query, (like_pattern, like_pattern, like_pattern))

    def insert_notifications_for_article(self, article_id):
        query_both = """
            INSERT INTO Notification (
                user_id,
                notification_setting_id,
                article_id,
                message,
                notification_date
            )
            SELECT
                ns.user_id,
                ns.notification_setting_id,
                cam.article_id,
                CONCAT('New article: ', a.title, ' - ', a.description),
                NOW()
            FROM category_article_mapping cam
            JOIN keyword_article_mapping kam ON cam.article_id = kam.article_id
            JOIN notification_setting ns 
                ON ns.category_id = cam.category_id AND ns.keyword_id = kam.keyword_id
            JOIN article a ON a.article_id = cam.article_id
            WHERE cam.article_id = %s
              AND ns.is_enabled = true
        """
        db_query(query_both, (article_id,))


        query_category_only = """
            INSERT INTO Notification (
                user_id,
                notification_setting_id,
                article_id,
                message,
                notification_date
            )
            SELECT
                ns.user_id,
                ns.notification_setting_id,
                cam.article_id,
                CONCAT('Category alert: ', a.title, ' - ', a.description),
                NOW()
            FROM category_article_mapping cam
            JOIN notification_setting ns 
                ON cam.category_id = ns.category_id AND ns.keyword_id IS NULL
            JOIN article a ON a.article_id = cam.article_id
            WHERE cam.article_id = %s
              AND ns.is_enabled = true
              AND NOT EXISTS (
                  SELECT 1 FROM notification_setting ns2
                  WHERE ns2.category_id = ns.category_id AND ns2.keyword_id IS NOT NULL
                        AND ns2.user_id = ns.user_id 
              )
        """
        db_query(query_category_only, (article_id,))


        query_keyword_only = """
            INSERT INTO Notification (
                user_id,
                notification_setting_id,
                article_id,
                message,
                notification_date
            )
            SELECT
                ns.user_id,
                ns.notification_setting_id,
                kam.article_id,
                CONCAT('Keyword match: ', a.title, ' - ', a.description),
                NOW()
            FROM keyword_article_mapping kam
            JOIN notification_setting ns 
                ON kam.keyword_id = ns.keyword_id AND ns.category_id IS NULL
            JOIN article a ON a.article_id = kam.article_id
            WHERE kam.article_id = %s
              AND ns.is_enabled = true
        """
        db_query(query_keyword_only, (article_id,))

    def get_reaction(self, user_id: int, article_id: int):
        query = """
            SELECT * FROM article_reaction
            WHERE user_id = %s AND article_id = %s
        """
        return db_query(query, (user_id, article_id))

    def insert_reaction(self, user_id: int, article_id: int, is_like: bool):
        query = """
            INSERT INTO article_reaction (user_id, article_id, is_like)
            VALUES (%s, %s, %s)
        """
        return db_query(query, (user_id, article_id, is_like))

    def update_reaction(self, user_id: int, article_id: int, is_like: bool):
        query = """
            UPDATE article_reaction
            SET is_like = %s, reaction_date = NOW()
            WHERE user_id = %s AND article_id = %s
        """
        return db_query(query, (is_like, user_id, article_id))

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
