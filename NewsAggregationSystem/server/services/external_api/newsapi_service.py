import requests
from NewsAggregationSystem.server.services.external_api.base_external_server_service import ExternalServerService
from NewsAggregationSystem.server.repos.external_server_repo import ExternalServerRepo
from NewsAggregationSystem.server.utilities.classify_category_utils import ClassifyCategory

class NewsAPIService(ExternalServerService):

    def fetch_the_news_articles(self, server_config):
        server_id, server_name, api_key, base_url, is_active, last_accessed = server_config

        url = f"{base_url}top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)

        articles = response.json().get("articles", [])

        for article in articles:
            title = article.get("title", "")
            description = article.get("description", "")
            content = article.get("content", "")
            combined_text = f"{title} {description} {content}".lower()

            category = ClassifyCategory.classify_category(combined_text)
            article["categories"] = category

        external_service_repo = ExternalServerRepo()
        external_service_repo.update_last_accessed(server_id)

        return articles


