from NewsAggregationSystem.server.database import db_query

class NotificationRepo:
    def get_user_notifications(self, user_id):
        query = """
            SELECT n.notification_id, n.user_id, n.message
            FROM Notification n
        """
        return db_query(query, (user_id))

    def get_all_notifications(self):
        query = """
            SELECT n.notification_id, n.user_id, n.message
            FROM Notification n
        """
        return db_query(query, ())

    def update_notification_date(self, notification_id):
        query = "UPDATE notification SET notification_date = NOW() WHERE notification_id = %s"
        db_query(query, (notification_id,))