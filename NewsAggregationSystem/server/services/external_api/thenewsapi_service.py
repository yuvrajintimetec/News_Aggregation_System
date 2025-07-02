import requests
from NewsAggregationSystem.server.services.external_api.base_external_server_service import ExternalServerService
from NewsAggregationSystem.server.repos.external_server_repo import ExternalServerRepo

class TheNewsApiService(ExternalServerService):

    def fetch_the_news_articles(self, server_config):
        server_id, server_name, api_key, base_url, is_active, last_accessed = server_config
        url = f"{base_url}all?api_token={api_key}"
        response = requests.get(url)

        external_service_repo = ExternalServerRepo()
        external_service_repo.update_last_accessed(server_id)

        return response.json().get("data", [])
