from server.services.extenal_server_service import ExternalServerService
from server.dtos.requests.external_server_update_request import ExternalServerUpdateRequest

class ExternalServerController:

    def __init__(self):
        self.external_server_service = ExternalServerService()

    def get_all_servers(self):
        return self.external_server_service.get_all_servers()

    def update_server(self, server_id: int, external_server_data: ExternalServerUpdateRequest):
        return self.external_server_service.update_server(server_id, external_server_data)
