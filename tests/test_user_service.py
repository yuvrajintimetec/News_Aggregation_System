import unittest
from unittest.mock import MagicMock
from NewsAggregationSystem.server.services.user_service import UserService
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        self.service.user_repo = MagicMock()

    def test_get_user_by_id_success(self):
        self.service.user_repo.get_user_by_id.return_value = (1, "Test User", "test@example.com", "user")
        result = self.service.get_user_by_id(1)
        self.assertEqual(result[1], "Test User")

    def test_get_user_by_id_not_found(self):
        self.service.user_repo.get_user_by_id.return_value = None
        with self.assertRaises(NotFoundException):
            self.service.get_user_by_id(2)

if __name__ == "__main__":
    unittest.main() 