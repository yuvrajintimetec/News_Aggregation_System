from NewsAggregationSystem.server.services.external_api.external_server_manager import ExternalServerManager
from NewsAggregationSystem.server.services.article_service import ArticleService
from fastapi import HTTPException, status
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.exceptions.update_failed_exception import UpdateFailedException

class ArticleController:

    def __init__(self):
        self.article_service = ArticleService()

    def fetch_and_store_all_articles(self):
        manager = ExternalServerManager()
        service = ArticleService()

        all_articles = manager.fetch_articles_from_active_servers()
        try:
            service.save_articles(all_articles)
            return {"message": "Articles saved successfully", "total": len(all_articles)}
        except (NotFoundException, InvalidDataException, UpdateFailedException) as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))


