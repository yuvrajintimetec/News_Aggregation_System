from NewsAggregationSystem.server.database import db_query

class ReactArticleRepo:
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
