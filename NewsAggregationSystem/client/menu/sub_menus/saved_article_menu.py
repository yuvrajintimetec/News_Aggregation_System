from datetime import datetime
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import article_details_response

class SavedArticleMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print(f"\nWelcome to the News Application, {self.user_data['name']}! Date: {datetime.now():%d-%b-%Y Time:%I:%M%p}")
        print("S A V E D\n")
        print("1. Back\n2. Logout\n3. Delete Article")

    def api_request(self):
        while True:
            articles = api_utilities.get_all_with_token("user/saved", {"Authorization": f"Bearer {self.access_token}"})
            self.show_menu()
            for article in articles:
                article_details_response(article)
            choice = input("Choose (1-3): ")
            if choice == "1":
                return
            elif choice == "2":
                return 0
            elif choice == "3":
                article_id = input("Enter Article ID to delete: ")
                api_utilities.delete_with_token("user/saved", int(article_id), {"Authorization": f"Bearer {self.access_token}"})
