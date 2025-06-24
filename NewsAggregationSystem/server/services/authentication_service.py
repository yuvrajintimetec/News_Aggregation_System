from NewsAggregationSystem.server.repos.user_repo import UserRepo
from NewsAggregationSystem.server.utilities.password_utils import PasswordUtils
from NewsAggregationSystem.server.utilities.jwt_utils import JWTUtils

class AuthenticationService:

    def __init__(self):
        self.user_repo = UserRepo()

    def register(self, name, email, password):
        user = self.user_repo.get_user_by_email(email)
        if user:
            return {"message": "User Already exists"}
        hashed_password = PasswordUtils.hash_password(password)
        role = "user"
        return self.user_repo.insert_user(name, email, hashed_password, role)

    def login(self, email, password):
        user = self.user_repo.get_user_by_email(email)
        if user:
            user_id, user_name, user_email, user_password, user_role = user[0]
            is_valid = PasswordUtils.verify_password(password, user_password)
            if is_valid:
                access_token = JWTUtils.create_access_token(data={"user_id": user_id, "user_role": user_role})
                return {
                    "message": "User login successfully",
                    "access_token": access_token
                }
        else:
            return {"message": "User not found"}
