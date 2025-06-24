from NewsAggregationSystem.server.services.article_service import ArticleService
from NewsAggregationSystem.server.services.user_service import UserService

class UserController:

    def __init__(self):
        self.article_service = ArticleService()
        self.user_service = UserService()

    def get_user_by_id(self, user_id):
        return self.user_service.get_user_by_id(user_id)

    def get_today_articles(self, user_info):
        return self.article_service.get_articles_for_today(user_info["user_id"])


    def get_articles_by_range(self, user_info, start_date, end_date, category):
        return self.article_service.get_articles_by_date_range(
            user_info["user_id"], start_date, end_date, category
        )


    def save_article_for_user(self, user_info, article_id):
        return self.article_service.save_article(user_info["user_id"], article_id)


    def get_saved_articles(self, user_info):
        return self.article_service.get_saved_articles(user_info["user_id"])


    def delete_saved_article(self, user_info, article_id):
        return self.article_service.delete_saved_article(user_info["user_id"], article_id)


    def search_articles(self, start_date, end_date, keyword, user_info):
        return self.article_service.search_articles_by_keyword(start_date, end_date, keyword, user_info["user_id"])
