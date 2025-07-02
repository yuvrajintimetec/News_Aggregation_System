from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.menu.sub_menus.notification_config_menu import NotificationConfigMenu
from NewsAggregationSystem.client.utilities import api_utilities

class NotificationMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print("\nN O T I F I C A T I O N S")
        print("1. View Notifications")
        print("2. Configure Notifications")
        print("3. Back")
        print("4. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Choose (1-4): ")
            if choice == "1":
                notifications = api_utilities.get_by_id("notifications", self.user_data["user_id"])
                print("\nNOTIFICATIONS")
                for note in notifications:
                    print(f"\n{note['title']}\n{note['message']}")
            elif choice == "2":
                NotificationConfigMenu(self.access_token, self.user_data).api_request()
            elif choice == "3":
                return
            elif choice == "4":
                exit()
