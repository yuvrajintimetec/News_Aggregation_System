import requests
from server.services.external_api.base_external_server_service import ExternalServerService
from server.repos.external_server_repo import ExternalServerRepo

class NewsAPIService(ExternalServerService):

    def fetch_the_news_articles(self, server_config):
        server_id, server_name, api_key, base_url, is_active, last_accessed = server_config

        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=05034717e582442eb81a992d8d507b67"
        response = requests.get(url)

        articles = response.json().get("articles", [])


        for article in articles:
            article["categories"] = ""

        article_repo = ExternalServerRepo(server_id)
        article_repo.update_last_accessed(server_id)

        return articles
