from NewsAggregationSystem.server.database import db_query

class NotificationRepo:
    def get_user_notifications(self, user_id):
        query = """
            SELECT n.notification_id, n.user_id, n.message
            FROM Notification n where n.user_id = %s and n.is_read = false
        """
        return db_query(query, (user_id,))

    def get_all_notifications(self):
        query = """
            SELECT n.notification_id, n.user_id, n.message
            FROM Notification n where n.is_read = false
        """
        return db_query(query, ())

    def update_notification_date(self, notification_id):
        query = "UPDATE notification SET notification_date = NOW() WHERE notification_id = %s"
        db_query(query, (notification_id,))

    def mark_as_read(self, notification_id):
        query = "UPDATE notification SET is_read = 1 WHERE notification_id = %s"
        db_query(query, (notification_id,))

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
               DISTINCT ns.user_id,
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
              DISTINCT ns.user_id,
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
               DISTINCT ns.user_id,
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


