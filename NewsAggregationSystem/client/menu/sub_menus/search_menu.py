from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities

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
        sort = input("Sort by (likes/dislikes): ")
        url = f"articles/search?keyword={keyword}&start={start}&end={end}&sort={sort}"

        articles = api_utilities.get_all(url)
        print(f"\nS E A R C H\nResults for “{keyword}”")
        self.show_menu()
        for article in articles:
            print(f"\nArticle Id: {article['article_id']} {article['title']}")
            print(f"{article['description']}\n")
            print(f"source : {article['source']}\nURL:\n{article['url']}\nBusiness: {article['category']}")
        choice = input("Choose (1-3): ")
        if choice == "3":
            article_id = input("Enter Article ID to save: ")
            api_utilities.create_with_token("user/save_article", {"article_id": int(article_id)}, {"Authorization": f"Bearer {self.access_token}"})
