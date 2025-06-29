from NewsAggregationSystem.server.repos.user_repo import UserRepo

class UserService:
    def __init__(self):
        self.user_repo = UserRepo()

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)
