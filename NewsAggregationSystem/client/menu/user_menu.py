from datetime import datetime
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.menu.sub_menus.headline_menu import HeadlineMenu
from NewsAggregationSystem.client.menu.sub_menus.saved_article_menu import SavedArticleMenu
from NewsAggregationSystem.client.menu.sub_menus.search_menu import SearchMenu
from NewsAggregationSystem.client.menu.sub_menus.notification_menu import NotificationMenu

class UserMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        now = datetime.now().strftime("%d-%b-%Y Time:%I:%M%p")
        print(f"\nWelcome to the News Application, {self.user_data['name']}! Date: {now}")
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
                headline_menu = HeadlineMenu(self.access_token, self.user_data).api_request()
                if headline_menu == "logout":
                    return "logout"
            elif choice == "2":
                save_article_menu = SavedArticleMenu(self.access_token, self.user_data).api_request()
                if save_article_menu == "logout":
                    return "logout"
            elif choice == "3":
                SearchMenu(self.access_token, self.user_data).api_request()
            elif choice == "4":
                NotificationMenu(self.access_token, self.user_data).api_request()
            elif choice == "5":
                print("Goodbye! You've been logged out.")
                return "logout"
            else:
                print("Invalid option. Please enter a number between 1 and 5.")
