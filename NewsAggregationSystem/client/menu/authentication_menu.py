from NewsAggregationSystem.client.menu.admin_menu import AdminMenu
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.menu.user_menu import UserMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import simple_response
from getpass import getpass
import sys

class AuthenticationMenu(BaseMenu):

    def show_menu(self):
        print("\nWelcome to the News Aggregator application. Please choose the options below.")
        print("1. Login")
        print("2. Sign up")
        print("3. Exit")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                user_data = {
                    "email": input("Email: ").strip(),
                    "password": input("Password: ")
                }
                login_data = api_utilities.create("auth/login", user_data)
                if ('access_token' in login_data) and (login_data['access_token'] is not None):
                    access_token = login_data['access_token']
                    headers = {
                        "Authorization": f"Bearer {access_token}"
                    }
                    user_data = api_utilities.get_all_with_token("user/profile", headers)
                    user_role =  user_data["user_role"]
                    if user_role == "admin":
                        role_menu = AdminMenu(access_token, user_data)
                    else:
                        role_menu = UserMenu(access_token, user_data)
                    simple_response(login_data)
                    return role_menu
                simple_response(login_data)

            elif choice == "2":
                user_data = {
                    "name": input("Username: ").strip(),
                    "email": input("Email: ").strip(),
                    "password": input("Password: ")
                }
                register_data = api_utilities.create("auth/register", user_data)
                simple_response(register_data)

            elif choice == "3":
                print("Thank you for using the News Aggregator app. Goodbye!")
                sys.exit()

            else:
                print("Invalid option. Please enter 1, 2, or 3.")
