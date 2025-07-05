from datetime import datetime
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import simple_response_containing_list, simple_response, reported_articles_details_response


class ReportedArticleMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print(f"\nWelcome to the News Application, {self.user_data['name']}! Date: {datetime.now():%d-%b-%Y Time:%I:%M%p}")
        print("S A V E D\n")
        print("1. Back\n2. Logout\n3. Hide article\n4. Hide article by keyword\n5. Hide article by category")

    def api_request(self):
        while True:
            response = api_utilities.get_all_with_token("admin/reported-articles", {"Authorization": f"Bearer {self.access_token}"})
            self.show_menu()
            reported_articles = simple_response_containing_list(response)
            if type(reported_articles) is list:
                for article in reported_articles:
                    reported_articles_details_response(article)
            else:
                print(reported_articles)
            choice = input("Choose (1-5): ")
            if choice == "1":
                return
            elif choice == "2":
                return "logout"
            elif choice == "3":
                article_id = input("Enter Article ID to hidden: ")
                hide_reported_article_response = api_utilities.create_with_token(f"admin/hide-reported-article/{article_id}", {}, {"Authorization": f"Bearer {self.access_token}"})
                simple_response(hide_reported_article_response)
            elif choice == "4":
                keyword = input("Enter keyword: ")
                hide_reported_article_response = api_utilities.create_with_token(
                    f"admin/hide-articles-by-keyword?keyword={keyword}", {}, {"Authorization": f"Bearer {self.access_token}"})
                simple_response(hide_reported_article_response)
            elif choice == "5":
                category = input("Enter the category: ")
                hide_reported_article_response = api_utilities.create_with_token(
                    f"admin/hide-articles-by-category?category={category}", {}, {"Authorization": f"Bearer {self.access_token}"})
                simple_response(hide_reported_article_response)
