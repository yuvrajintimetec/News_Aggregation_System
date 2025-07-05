from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.menu.sub_menus.notification_config_menu import NotificationConfigMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import simple_response_containing_list, \
    notification_details_response


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
                response = api_utilities.get_all_with_token("user/notifications", {"Authorization": f"Bearer {self.access_token}"})
                print("\nNOTIFICATIONS")
                notifications = simple_response_containing_list(response)
                if type(notifications) is list:
                    for notification in notifications:
                       notification_details_response(notification)
                else:
                    print(notifications)
            elif choice == "2":
                NotificationConfigMenu(self.access_token, self.user_data).api_request()
            elif choice == "3":
                return
            elif choice == "4":
                return "logout"
