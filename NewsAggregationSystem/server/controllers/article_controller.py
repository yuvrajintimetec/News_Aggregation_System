from NewsAggregationSystem.server.services.external_api.external_server_manager import ExternalServerManager
from NewsAggregationSystem.server.services.article_service import ArticleService

class ArticleController:

    def __init__(self):
        self.article_service = ArticleService()

    def fetch_and_store_all_articles(self):
        manager = ExternalServerManager()
        service = ArticleService()

        all_articles = manager.fetch_articles_from_active_servers()
        service.save_articles_with_category(all_articles)

        return {"message": "Articles saved successfully", "total": len(all_articles)}


