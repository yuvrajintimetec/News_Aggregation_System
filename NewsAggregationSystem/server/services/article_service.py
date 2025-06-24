from NewsAggregationSystem.server.repos.article_repo import ArticleRepo
from NewsAggregationSystem.server. repos.category_repo import CategoryRepo
from NewsAggregationSystem.server.repos.category_article_mapping_repo import CategoryArticleMappingRepo

class ArticleService:

    def __init__(self):
        self.article_repo = ArticleRepo()
        self.category_repo = CategoryRepo()
        self.mapping_repo = CategoryArticleMappingRepo()

    def save_articles_with_category(self, articles):
        for article in articles:
            title = article.get("title")
            description = article.get("description")
            content = article.get("content")
            url = article.get("url")
            published_at = article.get("published_at")
            source = article.get("source")
            categories = article.get("categories")
            server_id = article.get("server_id")

            article_data = {
                "title": title,
                "description": description,
                "content": content,
                "source": source,
                "url": url,
                "published_at": published_at,
                "server_id": server_id
            }
            self.article_repo.insert_article(article_data)
            article_id = self.article_repo.find_latest_article()[0]

            for category_name in categories:
                if category_name:
                    category = self.category_repo.find_category(category_name)
                    if category:
                        category_id, category_name = category[0]
                        self.mapping_repo.create_category_article_mapping(category_id, article_id)


    def get_articles_for_today(self, user_id):
        return self.article_repo.fetch_articles_by_date(user_id)

    def get_articles_by_date_range(self, user_id, start_date, end_date, category):
        return self.article_repo.fetch_articles_by_date_range(user_id, start_date, end_date, category)

    def save_article(self, user_id, article_id):
        return self.article_repo.save_article(user_id, article_id)

    def get_saved_articles(self, user_id):
        return self.article_repo.get_saved_articles(user_id)

    def delete_saved_article(self, user_id, article_id):
        return self.article_repo.delete_saved_article(user_id, article_id)

    def search_articles_by_keyword(self, start_date, end_date, keyword, user_id):
        return self.article_repo.search_articles( start_date, end_date, keyword)
