from datetime import datetime
from NewsAggregationSystem.client.menu.base_menu import BaseMenu
from NewsAggregationSystem.client.utilities import api_utilities
from NewsAggregationSystem.client.utilities.server_reponse_utils import article_details_response, \
    simple_response_containing_list, simple_response


class HeadlineMenu(BaseMenu):

    def __init__(self, access_token, user_data):
        self.access_token = access_token
        self.user_data = user_data

    def show_menu(self):
        print("\nHEADLINES")
        print("1. Today")
        print("2. Date range")
        print("3. Logout")

    def api_request(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.display_articles("user/headlines/today")
            elif choice == "2":
                start = input("Enter start date (YYYY-MM-DD): ")
                end = input("Enter end date (YYYY-MM-DD): ")
                category_response = api_utilities.get_all_with_token("category/", {"Authorization": f"Bearer {self.access_token}"})
                categories = simple_response_containing_list(category_response)
                if type(categories) is list:
                   print("1. all")
                   category_count = 2
                   category_map = {"1": "all"}
                   for category in categories:
                        category_name = category["category_name"]
                        category_name = category_name.lower()
                        print(f"{category_count}. {category_name}")
                        category_map.update({str(category_count): category_name})
                        category_count += 1
                   cat_choice = input("Choose a category: ")
                   if cat_choice in category_map:
                       category = category_map[cat_choice]
                   else:
                       print("Invalid choice")
                       continue
                   if category != 'all':
                       url = f"user/headlines/range?start_date={start}&end_date={end}&category={category}"
                   else:
                       url = f"user/headlines/range?start_date={start}&end_date={end}"
                   display = self.display_articles(url)
                   if display == "logout":
                       return "logout"
                else:
                   print(categories)
            elif choice == "3":
                return "logout"
            else:
                print("Invalid choice.")

    def display_articles(self, url):
        response = api_utilities.get_all_with_token(url, {"Authorization": f"Bearer {self.access_token}"})
        print("\nH E A D L I N E S")
        print("1. Back\n2. Logout\n3. Save Article\n4. React on an Article\n5. Report an Article")
        articles = simple_response_containing_list(response)
        if type(articles) is list:
            for article in articles:
                article_details_response(article)
        else:
            print(articles)
        action = input("Choose (1-5): ")
        if action == "1":
            return
        elif action == "2":
            return "logout"
        elif action == "3":
            article_id = input("Enter Article ID to save: ")
            saved_article_response = api_utilities.create_with_token(f"user/saved-article/{article_id}", {},{"Authorization": f"Bearer {self.access_token}"})
            simple_response(saved_article_response)
        elif action == "4":
            article_id = input("Enter Article ID to react: ")
            print("1. Like\n2. Dislike")
            choice = input("Choose(1-2): ")
            if choice not in ("1","2"):
                print("Invalid choice.")
                return
            endpoint = f"user/react/like/{article_id}" if choice == "1" else f"user/react/dislike/{article_id}"
            article_reaction_response = api_utilities.create_with_token(endpoint, {},{"Authorization": f"Bearer {self.access_token}"})
            simple_response(article_reaction_response)
        elif action == "5":
            article_id = input("Enter Article ID to report: ")
            report_reason = input("Enter reason for reporting the article: ")
            report_article_response = api_utilities.create_with_token(f"user/report-article/{article_id}", {"reason": report_reason},{"Authorization": f"Bearer {self.access_token}"})
            simple_response(report_article_response)
        else:
            print("Invalid choice.")

