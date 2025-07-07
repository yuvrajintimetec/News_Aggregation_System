from fastapi import HTTPException, status
from NewsAggregationSystem.server.repos.notification_repo import NotificationRepo
from NewsAggregationSystem.server.repos.user_repo import UserRepo
from NewsAggregationSystem.server.utilities.email_utils import send_email
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.utilities.logger import logger

class NotificationService:
    def __init__(self):
        self.notification_repo = NotificationRepo()
        self.user_repo = UserRepo()

    def get_notifications(self, user_id):
        notifications = self.notification_repo.get_user_notifications(user_id)
        if not notifications:
            raise NotFoundException(f"notifications not found")
        messages = []
        for notification in notifications:
            notification_id = notification[0]
            message = notification[2]
            messages.append(message)
            self.notification_repo.mark_as_read(notification_id)
        return messages

    async def send_notifications_by_email(self):
        logger.info("Starting to send notifications by email.")
        notifications = self.notification_repo.get_all_notifications()
        for notification in notifications:
            notification_id = notification[0]
            user_id = notification[1]
            user_email = self.user_repo.get_user_by_id(user_id)[2]
            message = notification[2]
            subject = "News Notification"
            await send_email(user_email, subject, message)
            logger.info(f"Sent notification email to user_id: {user_id}, email: {user_email}")
            self.notification_repo.mark_as_read(notification_id)
            self.notification_repo.update_notification_date(notification_id)
        logger.info("Completed sending notifications by email.")