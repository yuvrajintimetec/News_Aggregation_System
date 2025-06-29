from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities

class NotificationConfigMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print("\nCONFIGURE NOTIFICATIONS")
        print("1. Business")
        print("2. Entertainment")
        print("3. Sports")
        print("4. Technology")
        print("5. Keyword")
        print("6. Back")
        print("7. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-7): ")

            if choice in {"1", "2", "3", "4"}:
                categories = ["business", "entertainment", "sports", "technology"]
                category = categories[int(choice) - 1]
                state = input(f"Enable or disable notifications for {category}? (on/off): ")
                data = {"category": category, "enabled": state.lower() == "on"}
                api_utilities.create_with_token("notifications/configure_category", data, {"Authorization": f"Bearer {self.access_token}"})
            elif choice == "5":
                keyword = input("Enter keyword: ")
                state = input(f"Enable or disable keyword '{keyword}'? (on/off): ")
                data = {"keyword": keyword, "enabled": state.lower() == "on"}
                api_utilities.create_with_token("notifications/configure_keyword", data, {"Authorization": f"Bearer {self.access_token}"})
            elif choice == "6":
                return
            elif choice == "7":
                exit()
