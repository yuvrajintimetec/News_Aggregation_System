from NewsAggregationSystem.server.database import db_query

class NotificationSettingRepo:

    def upsert_notification_setting(self, user_id, category_id, keyword_id, is_enabled):
        check_query = """
            SELECT * FROM notification_setting
            WHERE user_id = %s AND category_id <=> %s AND keyword_id <=> %s
        """
        existing = db_query(check_query, (user_id, category_id, keyword_id))

        if existing:
            update_query = """
                UPDATE notification_setting
                SET is_enabled = %s
                WHERE user_id = %s AND category_id <=> %s AND keyword_id <=> %s
            """
            return db_query(update_query, (is_enabled, user_id, category_id, keyword_id))

        insert_query = """
            INSERT INTO notification_setting (user_id, category_id, keyword_id, is_enabled)
            VALUES (%s, %s, %s, %s)
        """
        return db_query(insert_query, (user_id, category_id, keyword_id, is_enabled))
