from NewsAggregationSystem.server.exceptions.invalid_credential_exception import InvalidCredentialsException
from NewsAggregationSystem.server.repos.user_repo import UserRepo
from NewsAggregationSystem.server.utilities.password_utils import PasswordUtils
from NewsAggregationSystem.server.utilities.jwt_utils import JWTUtils
from fastapi import HTTPException,status
from NewsAggregationSystem.server.exceptions.user_already_exist_exception import UserAlreadyExistsException
from NewsAggregationSystem.server.utilities.logger import logger

class AuthenticationService:

    def __init__(self):
        self.user_repo = UserRepo()

    def register(self, name, email, password):
        user = self.user_repo.get_user_by_email(email)
        if user:
            raise UserAlreadyExistsException("User already exists.")
        hashed_password = PasswordUtils.hash_password(password)
        role = "user"
        return self.user_repo.insert_user(name, email, hashed_password, role)

    def login(self, email, password):
        logger.info(f"Login attempt for email: {email}")
        user = self.user_repo.get_user_by_email(email)
        if user:
            user_id, user_name, user_email, user_password, user_role = user[0]
            is_valid = PasswordUtils.verify_password(password, user_password)
            if not is_valid:
                logger.warning(f"Failed login for email: {email} (invalid password)")
                raise InvalidCredentialsException("Wrong email or password.")

            access_token = JWTUtils.create_access_token(data={"user_id": user_id, "user_role": user_role})
            logger.info(f"User login successful for email: {email}")
            return {
                "message": "User login successfully",
                "access_token": access_token
            }
        else:
            logger.warning(f"Failed login for email: {email} (user not found)")
            raise InvalidCredentialsException("Wrong email or password.")
