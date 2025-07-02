from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import simple_response_containing_list, \
    article_details_response


class SearchMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print("\nS E A R C H")
        print("1. Back\n2. Logout\n3. Save Article")

    def api_request(self):
        keyword = input("Enter search keyword: ")
        start = input("Start Date (YYYY-MM-DD): ")
        end = input("End Date (YYYY-MM-DD): ")
        sort = input("Sort by (likes/dislikes, leave blank to skip): ")
        if sort:
            url = f"user/articles/search?keyword={keyword}&start_date={start}&end_date={end}&sort_by={sort}"
        else:
            url = f"user/articles/search?keyword={keyword}&start_date={start}&end_date={end}"

        response = api_utilities.get_all_with_token(url, {"Authorization": f"Bearer {self.access_token}"})
        print(f"\nS E A R C H\nResults for “{keyword}”")
        self.show_menu()
        articles = simple_response_containing_list(response)
        if type(articles) is list:
            for article in articles:
                article_details_response(article)
        else:
            print(articles)

        choice = input("Choose (1-3): ")
        if choice == "3":
            article_id = input("Enter Article ID to save: ")
            api_utilities.create_with_token("user/save_article", {"article_id": int(article_id)}, {"Authorization": f"Bearer {self.access_token}"})
