from NewsAggregationSystem.server.services.external_server_service import ExternalServerService
from NewsAggregationSystem.server.services.category_service import CategoryService

class AdminController:
    def __init__(self):
        self.external_server_service = ExternalServerService()
        self.category_service = CategoryService()

    def get_all_servers(self):
        servers = self.external_server_service.get_all_servers()
        keys = ["server_name", "api_key", "base_url", "is_active", "last_accessed"]
        server_response = [dict(zip(keys, server[1:])) for server in servers]
        return server_response

    def update_server(self, server_id, update_data):
        self.external_server_service.update_server(server_id, update_data)
        return {"message": "server details updated successfully"}

    def add_category(self, category):
        if self.category_service.add_category(category.category_name):
            return {"message": "category added successfully"}
        else:
            return {"error": "category already exists"}