from NewsAggregationSystem.server.repos.article_repo import ArticleRepo
from NewsAggregationSystem.server.repos.category_repo import CategoryRepo
from NewsAggregationSystem.server.repos.keyword_article_mapping_repo import KeywordArticleMappingRepo
from NewsAggregationSystem.server.repos.keyword_repo import KeywordRepo
from NewsAggregationSystem.server.repos.notification_setting_repo import NotificationSettingRepo
from fastapi import HTTPException, status

class NotificationSettingService:
    def __init__(self):
        self.repo = NotificationSettingRepo()
        self.category_repo = CategoryRepo()
        self.keyword_repo = KeywordRepo()
        self.article_repo = ArticleRepo()
        self.keyword_article_mapping_repo = KeywordArticleMappingRepo()

    def configure_notification(self, user_id, config):
        category_id = None
        keyword_id = None
        if config.is_enabled:
            is_enabled = config.is_enabled

        if config.category:
            category_name = config.category
            category = self.category_repo.find_category(category_name)
            if category:
                category_id = category[0][0]

        if config.keyword:
            keyword_name = config.keyword.lower()
            is_present, data = self.keyword_repo.find_or_create_keyword(keyword_name)
            articles = self.article_repo.search_articles_with_keyword(keyword_name)
            if not articles:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"No article found for this keyword name {keyword_name}")
            for article in articles:
                article_id = article[0]
                if is_present:
                    keyword_id = data[0][0]
                else:
                    keyword_id = self.keyword_repo.find_latest_keyword()[0]
                    existing_mapping = self.keyword_article_mapping_repo.get_keyword_article_mapping(keyword_id, article_id)
                    if not existing_mapping:
                        self.keyword_article_mapping_repo.create_keyword_article_mapping(keyword_id, article_id)
        if not category_id and not keyword_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Won't be able to insert the configuration")

        return self.repo.upsert_notification_setting(user_id, category_id, keyword_id, is_enabled)

    def get_all_categories_enability(self):
        categories = self.repo.fetch_all_categories_enability()
        if not categories:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No categories found")
        return [{"category_name": category[0], "is_enabled": category[1]} for category in categories]
