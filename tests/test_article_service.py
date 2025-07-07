import unittest
from unittest.mock import MagicMock, patch
from NewsAggregationSystem.server.services.article_service import ArticleService
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.update_failed_exception import UpdateFailedException

class TestArticleService(unittest.TestCase):
    def setUp(self):
        self.service = ArticleService()
        # Mock all repo dependencies
        self.service.article_repo = MagicMock()
        self.service.category_repo = MagicMock()
        self.service.mapping_repo = MagicMock()
        self.service.notification_repo = MagicMock()
        self.service.react_article_repo = MagicMock()
        self.service.read_article_history_repo = MagicMock()
        self.service.report_article_repo = MagicMock()

    def test_save_articles_invalid(self):
        with self.assertRaises(InvalidDataException):
            self.service.save_articles(None)
        with self.assertRaises(InvalidDataException):
            self.service.save_articles("notalist")

    def test_save_articles_valid(self):
        self.service.article_repo.find_latest_article.return_value = [1]
        self.service.article_repo.get_latest_status.return_value = [[True]]
        articles = [{
            "title": "Test Article",
            "description": "desc",
            "content": "content",
            "url": "url",
            "published_at": "2023-01-01T00:00:00.000Z",
            "source": "source",
            "categories": ["cat1"],
            "server_id": 1
        }]
        self.service.category_repo.find_category.return_value = [(1, "cat1")]
        self.service.mapping_repo.get_category_article_mapping.return_value = None
        self.service.save_articles(articles)
        self.service.article_repo.insert_article.assert_called()

    def test_react_like_to_article_new(self):
        self.service.react_article_repo.get_reaction.return_value = None
        self.service.react_article_repo.insert_like_reaction.return_value = True
        self.service.article_repo.update_likes.return_value = None
        result = self.service.react_like_to_article(1, 1)
        self.assertIn("message", result)

    def test_react_like_to_article_update(self):
        self.service.react_article_repo.get_reaction.return_value = [(1, 1, 1, None, False, True)]
        self.service.react_article_repo.update_like_reaction.return_value = True
        self.service.article_repo.update_likes.return_value = None
        result = self.service.react_like_to_article(1, 1)
        self.assertIn("message", result)

    def test_react_dislike_to_article_new(self):
        self.service.react_article_repo.get_reaction.return_value = None
        self.service.react_article_repo.insert_dislike_reaction.return_value = True
        self.service.article_repo.update_dislikes.return_value = None
        result = self.service.react_dislike_to_article(1, 1)
        self.assertIn("message", result)

    def test_react_dislike_to_article_update(self):
        self.service.react_article_repo.get_reaction.return_value = [(1, 1, 1, None, True, False)]
        self.service.react_article_repo.update_dislike_reaction.return_value = True
        self.service.article_repo.update_dislikes.return_value = None
        result = self.service.react_dislike_to_article(1, 1)
        self.assertIn("message", result)

    def test_hide_article_report_threshold_met(self):
        self.service.report_article_repo.count_reports_for_article.return_value = [(1, 5)]
        self.service.article_repo.set_article_hidden.return_value = None
        with patch("os.getenv", return_value="3"):
            result = self.service.hide_article_report(1)
            self.assertIn("message", result)

    def test_hide_article_report_threshold_not_met(self):
        self.service.report_article_repo.count_reports_for_article.return_value = [(1, 1)]
        with patch("os.getenv", return_value="3"):
            with self.assertRaises(InvalidDataException):
                self.service.hide_article_report(1)

if __name__ == "__main__":
    unittest.main() 