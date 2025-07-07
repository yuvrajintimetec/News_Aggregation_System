import unittest
from unittest.mock import MagicMock, patch
from NewsAggregationSystem.server.services.authentication_service import AuthenticationService
from NewsAggregationSystem.server.exceptions.user_already_exist_exception import UserAlreadyExistsException
from NewsAggregationSystem.server.exceptions.invalid_credential_exception import InvalidCredentialsException

class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        self.service = AuthenticationService()
        self.service.user_repo = MagicMock()

    def test_register_new_user(self):
        self.service.user_repo.get_user_by_email.return_value = None
        self.service.user_repo.insert_user.return_value = {"message": "User registration successfully"}
        result = self.service.register("Test User", "test@example.com", "password123")
        self.assertIn("message", result)

    def test_register_existing_user(self):
        self.service.user_repo.get_user_by_email.return_value = [1]
        with self.assertRaises(UserAlreadyExistsException):
            self.service.register("Test User", "test@example.com", "password123")

    @patch("NewsAggregationSystem.server.utilities.password_utils.PasswordUtils.verify_password", return_value=True)
    @patch("NewsAggregationSystem.server.utilities.jwt_utils.JWTUtils.create_access_token", return_value="token")
    def test_login_success(self, mock_jwt, mock_verify):
        self.service.user_repo.get_user_by_email.return_value = [(1, "Test User", "test@example.com", "hashed", "user")]
        result = self.service.login("test@example.com", "password123")
        self.assertIn("access_token", result)

    @patch("NewsAggregationSystem.server.utilities.password_utils.PasswordUtils.verify_password", return_value=False)
    def test_login_wrong_password(self, mock_verify):
        self.service.user_repo.get_user_by_email.return_value = [(1, "Test User", "test@example.com", "hashed", "user")]
        with self.assertRaises(InvalidCredentialsException):
            self.service.login("test@example.com", "wrongpassword")

    def test_login_user_not_found(self):
        self.service.user_repo.get_user_by_email.return_value = None
        with self.assertRaises(InvalidCredentialsException):
            self.service.login("notfound@example.com", "password123")

if __name__ == "__main__":
    unittest.main() 