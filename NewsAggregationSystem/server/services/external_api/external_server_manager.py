

from NewsAggregationSystem.server.services.external_api.newsapi_service import NewsAPIService
from NewsAggregationSystem.server.services.external_api.thenewsapi_service import TheNewsApiService
from NewsAggregationSystem.server.repos.external_server_repo import ExternalServerRepo

class ExternalServerManager:

    def __init__(self):
        self.repo = ExternalServerRepo()

    def get_service(self, server_name):
        if server_name == "News API":
            return NewsAPIService()
        if server_name == "The News API":
            return TheNewsApiService()
        return None

    def fetch_articles_from_active_servers(self):
        active_servers = self.repo.get_active_servers()
        all_articles = []

        for server in active_servers:
            server_id, server_name, api_key, base_url, is_active, last_accessed = server
            service = self.get_service(server_name)
            if service:
                articles = service.fetch_the_news_articles(server)
                for article in articles:
                    article["source"] = article.get("source", {}).get("name") if server_name == "News API" else article.get("source")
                    article["server_id"] = server_id
                    all_articles.append(article)

        return all_articles
