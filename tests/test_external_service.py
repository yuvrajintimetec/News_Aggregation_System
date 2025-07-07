import unittest
from unittest.mock import MagicMock
from NewsAggregationSystem.server.services.external_server_service import ExternalServerService
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException
from NewsAggregationSystem.server.exceptions.update_failed_exception import UpdateFailedException

class TestExternalServerService(unittest.TestCase):
    def setUp(self):
        self.service = ExternalServerService()
        self.service.external_server_repo = MagicMock()

    def test_get_all_servers_success(self):
        self.service.external_server_repo.get_all_servers.return_value = [(1, "server1", "key", "url", 1, None)]
        result = self.service.get_all_servers()
        self.assertEqual(result[0][1], "server1")

    def test_get_all_servers_not_found(self):
        self.service.external_server_repo.get_all_servers.return_value = []
        with self.assertRaises(NotFoundException):
            self.service.get_all_servers()

    def test_update_server_success(self):
        self.service.external_server_repo.update_server.return_value = True
        result = self.service.update_server(1, {"server_name": "new"})
        self.assertTrue(result)

    def test_update_server_failure(self):
        self.service.external_server_repo.update_server.return_value = False
        with self.assertRaises(UpdateFailedException):
            self.service.update_server(1, {"server_name": "fail"})

if __name__ == "__main__":
    unittest.main() 