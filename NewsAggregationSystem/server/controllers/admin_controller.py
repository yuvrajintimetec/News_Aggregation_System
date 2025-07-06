from fastapi import HTTPException, status

from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.update_failed_exception import UpdateFailedException
from NewsAggregationSystem.server.services.article_service import ArticleService
from NewsAggregationSystem.server.services.external_server_service import ExternalServerService
from NewsAggregationSystem.server.services.category_service import CategoryService


class AdminController:
    def __init__(self):
        self.external_server_service = ExternalServerService()
        self.category_service = CategoryService()
        self.article_service = ArticleService()

    def get_all_servers(self):
        try:
            servers = self.external_server_service.get_all_servers()
            keys = ["server_name", "api_key", "base_url", "is_active", "last_accessed"]
            server_response = [dict(zip(keys, server[1:])) for server in servers]
            return {"message": server_response}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def update_server(self, server_id, update_data):
        try:
            updated_info = self.external_server_service.update_server(server_id, update_data)
            return {"message": updated_info["message"]}
        except UpdateFailedException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    def add_category(self, category):
        try:
            if self.category_service.add_category(category.category_name):
                return {"message": "category added successfully"}
            else:
                return {"error": "category already exists"}
        except InvalidDataException as error:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error))

    def check_reported_articles(self):
        articles = self.article_service.check_article_report()
        keys = [
        "reported_article_id",
        "article_id",
        "user_id",
        "report_reason",
        "reported_at"
       ]
        print(articles)
        article_response = [dict(zip(keys, article)) for article in articles]
        return {"message": article_response}

    def hide_reported_article(self, article_id):
       return self.article_service.hide_article_report(article_id)

    def hide_reported_articles_with_keyword(self, keyword):
        return self.article_service.hide_reported_articles_with_keyword(keyword)

    def hide_articles_by_category(self, category_name: str):
        result = self.article_service.hide_articles_by_category(category_name)
        if "message" in result:
            return {"message": result["message"]}
        else:
            return {"error": result["error"]}
