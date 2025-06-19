import requests
from server.services.external_api.base_external_server_service import ExternalServerService
from server.repos.external_server_repo import ExternalServerRepo

class TheNewsApiService(ExternalServerService):

    def fetch_the_news_articles(self, server_config):
        server_id, server_name, api_key, base_url, is_active, last_accessed = server_config
        url = f"https://api.thenewsapi.com/v1/news/all?api_token=5Q9gC1IFAHnHVaWXE8vgJuikQlgtEGMPqixBvFAn"
        response = requests.get(url)

        article_repo = ExternalServerRepo(server_id)
        article_repo.update_last_accessed(server_id)

        return response.json().get("data", [])
