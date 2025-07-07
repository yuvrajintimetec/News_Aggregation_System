from fastapi import HTTPException, status

from NewsAggregationSystem.server.repos.user_repo import UserRepo
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException

class UserService:
    def __init__(self):
        self.user_repo = UserRepo()

    def get_user_by_id(self, user_id):
        user_details = self.user_repo.get_user_by_id(user_id)
        if not user_details:
            raise NotFoundException(f"User details not found")
        return user_details
