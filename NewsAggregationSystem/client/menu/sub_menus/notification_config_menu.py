from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import simple_response, simple_response_containing_list


class NotificationConfigMenu(BaseMenu):
    category_map = {}

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print("\nCONFIGURE NOTIFICATIONS")
        category_response = api_utilities.get_all_with_token("notification-setting/category-enability/", {"Authorization": f"Bearer {self.access_token}"})
        categories = simple_response_containing_list(category_response)
        category_count = 1
        if type(categories) is list:
            for category in categories:
                category_name = category["category_name"]
                is_enabled = "ENABLED" if category["is_enabled"] else "DISABLED"
                category_name = category_name.lower()
                print(f"{category_count}. {category_name} - {is_enabled}")
                self.category_map.update({str(category_count): category_name})
                category_count += 1
        print(f"{category_count}. Keyword")
        category_count += 1
        print(f"{category_count}. Back")
        category_count += 1
        print(f"{category_count}. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice in self.category_map:
                category = self.category_map[choice]
                keyword = input("Enter keyword(leave blank space if not require): ")
                state = input(f"Enable or disable notifications for {category}? (true/false): ")
                if keyword:
                    keyword = keyword.lower()
                    data = {"category": category,  "keyword":keyword,  "is_enabled": state}
                else:
                    data = {"category": category, "is_enabled": state}
                is_configure = api_utilities.create_with_token("user/notifications/configure", data, {"Authorization": f"Bearer {self.access_token}"})
                simple_response(is_configure)
            elif choice == str(len(self.category_map) + 1):
                keyword = input("Enter keyword: ")
                state = input(f"Enable or disable keyword '{keyword}'? (true/false): ")
                data = {"keyword": keyword, "is_enabled": state}
                is_configure = api_utilities.create_with_token("user/notifications/configure", data, {"Authorization": f"Bearer {self.access_token}"})
                simple_response(is_configure)
            elif choice == str(len(self.category_map) + 2):
                return
            elif choice == str(len(self.category_map) + 3):
                return "logout"
            else:
                print("Invalid choice.")
