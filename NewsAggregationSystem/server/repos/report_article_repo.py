from NewsAggregationSystem.server.database import db_query

class ReportArticleRepo:
    def insert_article_report(self, article_id: int, user_id: int, reason: str):
        query = """
            INSERT INTO reported_article (article_id, user_id, report_reason)
            VALUES (%s, %s, %s)
        """
        return db_query(query, (article_id, user_id, reason))

    def update_article_report(self, article_id: int, user_id: int, reason: str):
        query = """
            UPDATE reported_article
            SET report_reason = %s, reported_at = NOW()
            WHERE article_id = %s AND user_id = %s
        """
        return db_query(query, (reason, article_id, user_id))

    def get_article_report(self, article_id: int, user_id: int):
        query = """
            SELECT * FROM reported_article
            WHERE article_id = %s AND user_id = %s
        """
        return db_query(query, (article_id, user_id))

    def count_reports_for_article(self, article_id):
        query = "SELECT article_id, COUNT(*) as count FROM reported_article where article_id = %s group by article_id"
        return db_query(query, (article_id,))

    def get_all_reported_articles(self):
        query = "SELECT * FROM reported_article"
        return db_query(query, ())