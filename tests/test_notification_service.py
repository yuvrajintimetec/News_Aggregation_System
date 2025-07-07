import unittest
from unittest.mock import MagicMock, patch, AsyncMock
from NewsAggregationSystem.server.services.notification_service import NotificationService
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
import asyncio

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.service = NotificationService()
        self.service.notification_repo = MagicMock()
        self.service.user_repo = MagicMock()

    def test_get_notifications_success(self):
        self.service.notification_repo.get_user_notifications.return_value = [
            (1, 2, "Test message")
        ]
        self.service.notification_repo.mark_as_read.return_value = None
        messages = self.service.get_notifications(2)
        self.assertIn("Test message", messages)

    def test_get_notifications_not_found(self):
        self.service.notification_repo.get_user_notifications.return_value = []
        with self.assertRaises(NotFoundException):
            self.service.get_notifications(2)


if __name__ == "__main__":
    unittest.main() 