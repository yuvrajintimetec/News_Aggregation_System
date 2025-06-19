
from client.menu.base_menu import BaseMenu
from client.utilities import api_utilities
import sys
from datetime import datetime

class UserMenu(BaseMenu):

    def show_menu(self):
        now = datetime.now().strftime("%d-%b-%Y \nTime:%I:%M%p")
        print(f"\nWelcome to the News Application, Suresh! Date: {now}")
        print("Please choose the options below:")
        print("1. Headlines")
        print("2. Saved Articles")
        print("3. Search")
        print("4. Notifications")
        print("5. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                response = api_utilities.get_all("articles/headlines")
                print("Headlines:\n", response)

            elif choice == "2":
                response = api_utilities.get_by_id("saved-articles", int(user_id))
                print("Saved Articles:\n", response)

            elif choice == "3":
                keyword = input("Enter keyword to search: ")
                response = api_utilities.get_all(f"articles/search?keyword={keyword}")
                print("Search Results:\n", response)

            elif choice == "4":
                response = api_utilities.get_by_id("notifications", int(user_id))
                print("Notifications:\n", response)

            elif choice == "5":
                print("Goodbye! You've been logged out.")
                sys.exit()

            else:
                print("Invalid option. Please enter a number between 1 and 5.")
