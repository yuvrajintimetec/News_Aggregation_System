import bcrypt
from NewsAggregationSystem.server.utilities.logger import logger

class PasswordUtils:

    @staticmethod
    def hash_password(plain_password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        logger.info("Password hashed.")
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        result = bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        logger.info(f"Password verification attempted. Result: {'success' if result else 'failure'}.")
        return result
