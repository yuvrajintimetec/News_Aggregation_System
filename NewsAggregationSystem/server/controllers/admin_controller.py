from NewsAggregationSystem.server.services.external_server_service import ExternalServerService
from NewsAggregationSystem.server.services.category_service import CategoryService

class AdminController:
    def __init__(self):
        self.external_server_service = ExternalServerService()
        self.category_service = CategoryService()

    def get_all_servers(self):
        return self.external_server_service.get_all_servers()

    def update_server(self, server_id, update_data):
        return self.external_server_service.update_server(server_id, update_data)

    def add_category(self, category):
        return self.category_service.add_category(category.category_name)