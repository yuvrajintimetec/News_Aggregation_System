import unittest
from unittest.mock import MagicMock
from NewsAggregationSystem.server.services.notification_setting_service import NotificationSettingService
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException

class DummyConfig:
    def __init__(self, is_enabled=True, category=None, keyword=None):
        self.is_enabled = is_enabled
        self.category = category
        self.keyword = keyword

class TestNotificationSettingService(unittest.TestCase):
    def setUp(self):
        self.service = NotificationSettingService()
        self.service.repo = MagicMock()
        self.service.category_repo = MagicMock()
        self.service.keyword_repo = MagicMock()
        self.service.article_repo = MagicMock()
        self.service.keyword_article_mapping_repo = MagicMock()

    def test_get_all_categories_enability_success(self):
        self.service.repo.fetch_all_categories_enability.return_value = [("cat1", True)]
        result = self.service.get_all_categories_enability()
        self.assertEqual(result[0]["category_name"], "cat1")
        self.assertTrue(result[0]["is_enabled"])

    def test_get_all_categories_enability_not_found(self):
        self.service.repo.fetch_all_categories_enability.return_value = []
        with self.assertRaises(NotFoundException):
            self.service.get_all_categories_enability()

    def test_configure_notification_success_category(self):
        config = DummyConfig(is_enabled=True, category="cat1", keyword=None)
        self.service.category_repo.find_category.return_value = [(1, "cat1")]
        self.service.repo.upsert_notification_setting.return_value = True
        result = self.service.configure_notification(1, config)
        self.assertTrue(result)

    def test_configure_notification_success_keyword(self):
        config = DummyConfig(is_enabled=True, category=None, keyword="news")
        self.service.keyword_repo.find_or_create_keyword.return_value = (True, [(2, "news")])
        self.service.article_repo.search_articles_with_keyword.return_value = [(3,)]
        self.service.repo.upsert_notification_setting.return_value = True
        result = self.service.configure_notification(1, config)
        self.assertTrue(result)

    def test_configure_notification_no_articles_for_keyword(self):
        config = DummyConfig(is_enabled=True, category=None, keyword="news")
        self.service.keyword_repo.find_or_create_keyword.return_value = (True, [(2, "news")])
        self.service.article_repo.search_articles_with_keyword.return_value = []
        with self.assertRaises(NotFoundException):
            self.service.configure_notification(1, config)

    def test_configure_notification_invalid(self):
        config = DummyConfig(is_enabled=True, category=None, keyword=None)
        with self.assertRaises(InvalidDataException):
            self.service.configure_notification(1, config)

if __name__ == "__main__":
    unittest.main() 