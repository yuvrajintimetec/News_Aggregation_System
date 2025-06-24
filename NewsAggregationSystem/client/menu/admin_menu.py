from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
import sys
from datetime import datetime

class AdminMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.user_data = user_data
        self.access_token = access_token

    def show_menu(self):
        print(f"\nWelcome to the News Application, {self.user_data['name']} Date: {datetime.now()}")
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
                response = api_utilities.get_all_with_token("admin/list_external_server", headers)
                print("All External Servers:\n", response)

            elif choice == "2":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                response = api_utilities.get_all_with_token("admin/list_external_server", headers)
                print("Server Details:\n", response)

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

                response = api_utilities.update_with_token("admin/update_external_server", server_id, data, headers)
                print("Update Response:\n", response)

            elif choice == "4":
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
                category_name = input("Enter new category name: ")
                response =api_utilities.create_with_token("admin/add_category", {"category_name": category_name}, headers)
                print("Add Category Response:\n", response)

            elif choice == "5":

                sys.exit()

            else:
                print("Invalid option. Please enter a number between 1 and 5.")
