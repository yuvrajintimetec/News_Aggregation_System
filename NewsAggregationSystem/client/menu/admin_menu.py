

from client.menu.base_menu import BaseMenu
from client.utilities import api_utilities
import sys

class AdminMenu(BaseMenu):

    def show_menu(self):
        print("\nAdmin Dashboard - News Aggregator")
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
                response = api_utilities.get_all("external-server")
                print("All External Servers:\n", response)

            elif choice == "2":
                server_id = int(input("Enter Server ID to view: "))
                response = api_utilities.get_by_id("external-server", server_id)
                print("Server Details:\n", response)

            elif choice == "3":
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

                response = api_utilities.update("external-server", server_id, data)
                print("Update Response:\n", response)

            elif choice == "4":
                category_name = input("Enter new category name: ")
                response =api_utilities.create("category", {"category_name": category_name})
                print("Add Category Response:\n", response)

            elif choice == "5":
                print("Logging out. Goodbye, Admin!")
                sys.exit()

            else:
                print("Invalid option. Please enter a number between 1 and 5.")
