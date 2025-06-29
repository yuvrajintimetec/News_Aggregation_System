from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import external_server_details_response,external_server_status_response, simple_response
import sys
from datetime import datetime

class AdminMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.user_data = user_data
        self.access_token = access_token

    def show_menu(self):
        now = datetime.now().strftime("%d-%b-%Y Time:%I:%M%p")
        print(f"\nWelcome to the News Application, {self.user_data['name']}! Date: {now}")
        print("1. View the list of external servers and status")
        print("2. View the external server’s details")
        print("3. Update/Edit the external server’s details")
        print("4. Add new News Category")
        print("5. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                server_details = api_utilities.get_all_with_token("admin/list_external_server", headers)
                for server_detail in server_details:
                    external_server_status_response(server_detail)

            elif choice == "2":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                server_details = api_utilities.get_all_with_token("admin/list_external_server", headers)
                for server_detail in server_details:
                    external_server_details_response(server_detail)

            elif choice == "3":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                server_id = int(input("Enter Server ID to update: "))
                api_key = input("New API Key (leave blank to skip): ")
                base_url = input("New Base URL (leave blank to skip): ")
                is_active = input("Is Active (true/false, leave blank to skip): ")

                data = {}
                if api_key:
                    data["api_key"] = api_key
                if base_url:
                    data["base_url"] = base_url
                if is_active:
                    data["is_active"] = is_active.lower() == "true"

                updated_server_details = api_utilities.update_with_token("admin/update_external_server", server_id, data, headers)
                simple_response(updated_server_details)

            elif choice == "4":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                category_name = input("Enter new category name: ")
                add_category_data =api_utilities.create_with_token("admin/add_category", {"category_name": category_name}, headers)
                simple_response(add_category_data)

            elif choice == "5":
                print("Logging out from Admin console....")
                return

            else:
                print("Invalid option. Please enter a number between 1 and 5.")
