from NewsAggregationSystem.server.services.article_service import ArticleService
from NewsAggregationSystem.server.services.user_service import UserService
from NewsAggregationSystem.server.services.notification_service import NotificationService
from NewsAggregationSystem.server.services.notification_setting_service import NotificationSettingService
from fastapi import HTTPException, status
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.exceptions.update_failed_exception import UpdateFailedException


class UserController:

    def __init__(self):
        self.article_service = ArticleService()
        self.user_service = UserService()
        self.notification_service = NotificationService()
        self.notification_setting_service = NotificationSettingService()

    def get_user_by_id(self, user_id):
        try:
            user =  self.user_service.get_user_by_id(user_id)
            return {
                "name": user[1],
                "user_role": user[3]
            }
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def get_today_articles(self, user_info):
        try:
            articles = self.article_service.get_articles_for_today(user_info["user_id"])
            keys = [
                "article_id",
                "title",
                "description",
                "content",
                "source",
                "url",
                "published_at",
                "server_id"
            ]
            article_response = [dict(zip(keys, article)) for article in articles]
            return {"message": article_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def get_articles_by_range(self, user_info, start_date, end_date, category):
        try:
            articles = self.article_service.get_articles_by_date_range(
                user_info["user_id"], start_date, end_date, category
            )
            keys = [
                "article_id",
                "title",
                "description",
                "content",
                "source",
                "url",
                "published_at",
                "server_id"
            ]
            article_response = [dict(zip(keys, article)) for article in articles]
            return {"message": article_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def save_article_for_user(self, user_info, article_id):
        try:
            response =  self.article_service.save_article(user_info["user_id"], article_id)
            if "message" in response:
                return {"message": response["message"]}
            else:
                return {"error": response["error"]}
        except UpdateFailedException as error:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

    def get_saved_articles(self, user_info):
        try:
            articles =  self.article_service.get_saved_articles(user_info["user_id"])
            keys = [
                "article_id",
                "title",
                "description",
                "content",
                "source",
                "url",
                "published_at",
                "server_id"
            ]
            article_response = [dict(zip(keys, article)) for article in articles]
            return {"message": article_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def get_reacted_articles(self, user_info):
        try:
            articles =  self.article_service.get_reacted_articles(user_info["user_id"])
            keys = [
                "article_id",
                "title",
                "description",
                "content",
                "source",
                "url",
                "published_at",
                "server_id"
            ]
            article_response = [dict(zip(keys, article)) for article in articles]
            return {"message": article_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def delete_saved_article(self, user_info, article_id):
        try:
            if self.article_service.delete_saved_article(user_info["user_id"], article_id):
                return {"message": f"Article with id {article_id} deleted Successfully"}
            else:
                return {"error": f"Article not found"}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def search_articles(self, start_date, end_date, keyword, sort_by, user_info):
        try:
            articles = self.article_service.search_articles_by_keyword(start_date, end_date, keyword, sort_by, user_info["user_id"])
            keys = [
                "article_id",
                "title",
                "description",
                "content",
                "source",
                "url",
                "published_at",
                "server_id"
            ]
            article_response = [dict(zip(keys, article[0:8])) for article in articles]
            return {"message":article_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def view_notifications(self, user_id):
        try:
            messages =  self.notification_service.get_notifications(user_id)
            return {"message": messages}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def configure(self, user_id, config):
        try:
            if self.notification_setting_service.configure_notification(user_id, config):
                return {"message": "Configuration done successfully"}
            else:
                return {"error": "Configuration setup failed"}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
        except InvalidDataException as error:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error))


    def react_like_to_article(self, user_id: int, article_id: int):
        try:
            response = self.article_service.react_like_to_article(user_id, article_id)
            if "message" in response:
                return {"message": response["message"]}
            else:
                return {"error": response["error"]}
        except UpdateFailedException as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    def react_dislike_to_article(self, user_id: int, article_id: int):
        try:
            response = self.article_service.react_dislike_to_article(user_id, article_id)
            if "message" in response:
                return {"message": response["message"]}
            else:
                return {"error": response["error"]}
        except UpdateFailedException as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    def report_article(self, article_id: int, user_id: int, reason: str):
        try:
            return self.article_service.submit_article_report(article_id, user_id, reason)
        except UpdateFailedException as error:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

