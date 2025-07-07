import unittest
from unittest.mock import MagicMock
from NewsAggregationSystem.server.services.category_service import CategoryService
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.category_already_exist import CategoryAlreadyExistException

class TestCategoryService(unittest.TestCase):
    def setUp(self):
        self.service = CategoryService()
        self.service.category_repo = MagicMock()

    def test_add_category_success(self):
        self.service.category_repo.find_category.return_value = None
        self.service.category_repo.insert_category.return_value = True
        result = self.service.add_category("cat1")
        self.assertTrue(result)

    def test_add_category_already_exists(self):
        self.service.category_repo.find_category.return_value = [(1, "cat1")]
        with self.assertRaises(CategoryAlreadyExistException):
            self.service.add_category("cat1")

    def test_get_all_categories_success(self):
        self.service.category_repo.fetch_all_categories.return_value = [(1, "cat1")]
        result = self.service.get_all_categories()
        self.assertEqual(result[0]["category_name"], "cat1")

    def test_get_all_categories_not_found(self):
        self.service.category_repo.fetch_all_categories.return_value = []
        with self.assertRaises(NotFoundException):
            self.service.get_all_categories()

if __name__ == "__main__":
    unittest.main() 