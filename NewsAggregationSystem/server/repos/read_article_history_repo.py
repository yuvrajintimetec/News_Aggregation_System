from NewsAggregationSystem.server.database import db_query

class ReadArticleHistoryRepo:
    def get_article_read_history(self, user_id: int, article_id: int):
        query = """
            SELECT * FROM read_article_history
            WHERE user_id = %s AND article_id = %s
        """
        return db_query(query, (user_id, article_id))

    def insert_article_read_history(self, user_id: int, article_id: int):
        query = """
            INSERT INTO read_article_history(user_id, article_id)
            VALUES (%s, %s)
        """
        return db_query(query, (user_id, article_id))

    def update_article_read_date(self, user_id: int, article_id: int):
        query = """
            UPDATE read_article_history
            SET article_read_date = NOW()
            WHERE user_id = %s AND article_id = %s
        """
        return db_query(query, (user_id, article_id))
