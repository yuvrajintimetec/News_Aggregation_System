import requests
from NewsAggregationSystem.server.repos.external_server_repo import ExternalServerRepo

class ExternalServerService:

    def __init__(self):
        self.external_server_repo = ExternalServerRepo()

    def get_all_servers(self):
        servers = self.external_server_repo.get_all_servers()
        return servers


    def update_server(self, server_id, external_server_data):
        updated_data =  self.external_server_repo.update_server(server_id, external_server_data)
        if updated_data == 0:
            return {"error": f"Server with ID {server_id} not found or no changes made"}

        return {"message": "Server details updated successfully"}


