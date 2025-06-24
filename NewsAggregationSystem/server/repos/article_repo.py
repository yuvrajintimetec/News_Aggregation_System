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

    def find_article(self):
        query = '''Select * from article'''
        return db_query(query, ())[0]

    def find_latest_article(self):
        query = '''Select * from article order by article_id desc limit 1'''
        return db_query(query, ())[0]

    def fetch_articles_by_date(self, user_id):
        query = """
            SELECT * FROM article
            WHERE DATE(published_at) = CURDATE()
        """
        return db_query(query)

    def fetch_articles_by_date_range(self, user_id, start_date, end_date, category):
        if category.lower() == "all":
            query = """
                SELECT * FROM article
                WHERE DATE(published_at) BETWEEN %s AND %s
            """
            return db_query(query, (start_date, end_date))
        else:
            query = """
                SELECT a.* FROM article a
                JOIN category_article_mapping cam ON a.article_id = cam.article_id
                JOIN category c ON cam.category_id = c.category_id
                WHERE DATE(a.published_at) BETWEEN %s AND %s AND c.category_name = %s
            """
            return db_query(query, (start_date, end_date, category))

    def save_article(self, user_id, article_id):
        query = """
            INSERT INTO saved_article (user_id, article_id)
            VALUES (%s, %s)
        """
        return db_query(query, (user_id, article_id))

    def get_saved_articles(self, user_id):
        query = """
            SELECT a.* FROM article a
            JOIN saved_article usa ON a.article_id = usa.article_id
            WHERE usa.user_id = %s
        """
        return db_query(query, (user_id,))

    def delete_saved_article(self, user_id, article_id):
        query = """
               DELETE FROM saved_article
               WHERE user_id = %s AND article_id = %s
           """
        return db_query(query, (user_id, article_id))

    def search_articles(self, start_date, end_date, keyword):
        query = """
               SELECT * FROM article
               WHERE  DATE(published_at) BETWEEN %s AND %s and title LIKE %s OR description LIKE %s OR content LIKE %s 
           """
        like_pattern = f"%{keyword}%"
        return db_query(query, (start_date, end_date, like_pattern, like_pattern, like_pattern))



