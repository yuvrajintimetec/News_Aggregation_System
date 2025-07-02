from datetime import datetime
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import article_details_response, \
    simple_response_containing_list


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
            response = api_utilities.get_all_with_token("user/saved-articles", {"Authorization": f"Bearer {self.access_token}"})
            self.show_menu()
            articles = simple_response_containing_list(response)
            if type(articles) is list:
                for article in articles:
                    article_details_response(article)
            else:
                print(articles)
            choice = input("Choose (1-3): ")
            if choice == "1":
                return
            elif choice == "2":
                return "logout"
            elif choice == "3":
                article_id = input("Enter Article ID to delete: ")
                api_utilities.delete_with_token("user/saved-article", int(article_id), {"Authorization": f"Bearer {self.access_token}"})
