from NewsAggregationSystem.server.repos.notification_repo import NotificationRepo
from NewsAggregationSystem.server.repos.user_repo import UserRepo
from NewsAggregationSystem.server.utilities.email_utils import send_email
import random

class NotificationService:
    def __init__(self):
        self.notification_repo = NotificationRepo()
        self.user_repo = UserRepo()

    def get_notifications(self, user_id):
        notifications = self.notification_repo.get_user_notifications(user_id)
        messages = []
        for notification in notifications:
            message = notification[2]
            messages.append(message)
        return messages

    async def send_notifications_by_email(self):
        notifications = self.notification_repo.get_all_notifications()
        notification = random.choice(notifications)
        notification_id = notification[0]
        user_id = notification[1]
        user_email = self.user_repo.get_user_by_id(user_id)[2]
        message = notification[2]
        subject = "News Notification"
        self.notification_repo.update_notification_date(notification_id)
        if user_id == 8:
            await send_email(user_email, subject, message)