import unittest
from NewsAggregationSystem.server.utilities.classify_category_utils import ClassifyCategory
from NewsAggregationSystem.server.utilities.password_utils import PasswordUtils
from NewsAggregationSystem.server.utilities.jwt_utils import JWTUtils
from datetime import timedelta

class TestUtils(unittest.TestCase):
    def test_classify_category_business(self):
        self.assertEqual(ClassifyCategory.classify_category("stock market news"), "Business")

    def test_classify_category_entertainment(self):
        self.assertEqual(ClassifyCategory.classify_category("movie music awards"), "Entertainment")

    def test_classify_category_sports(self):
        self.assertEqual(ClassifyCategory.classify_category("game match score"), "Sports")

    def test_classify_category_technology(self):
        self.assertEqual(ClassifyCategory.classify_category("tech gadget ai"), "Technology")

    def test_classify_category_general(self):
        self.assertEqual(ClassifyCategory.classify_category("random unrelated text"), "General")

    def test_password_hash_and_verify(self):
        password = "securepassword123"
        hashed = PasswordUtils.hash_password(password)
        self.assertTrue(PasswordUtils.verify_password(password, hashed))
        self.assertFalse(PasswordUtils.verify_password("wrongpassword", hashed))

    def test_jwt_create_and_decode(self):
        data = {"user_id": 1, "role": "admin"}
        token = JWTUtils.create_access_token(data, expires_delta=timedelta(minutes=1))
        decoded = JWTUtils.decode_access_token(token)
        self.assertEqual(decoded["user_id"], 1)
        self.assertEqual(decoded["role"], "admin")

if __name__ == "__main__":
    unittest.main() 