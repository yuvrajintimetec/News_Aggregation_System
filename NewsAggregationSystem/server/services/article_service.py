from NewsAggregationSystem.server.repos.read_article_history_repo import ReadArticleHistoryRepo, ReadArticleHistoryRepo
from NewsAggregationSystem.server.repos.article_repo import ArticleRepo
from NewsAggregationSystem.server. repos.category_repo import CategoryRepo
from NewsAggregationSystem.server.repos.category_article_mapping_repo import CategoryArticleMappingRepo
from NewsAggregationSystem.server.repos.notification_repo import NotificationRepo
from NewsAggregationSystem.server.repos.react_article_repo import ReactArticleRepo
from NewsAggregationSystem.server.repos.report_article_repo import ReportArticleRepo
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status

load_dotenv()

class ArticleService:

    def __init__(self):
        self.article_repo = ArticleRepo()
        self.category_repo = CategoryRepo()
        self.mapping_repo = CategoryArticleMappingRepo()
        self.report_article_repo = ReportArticleRepo()
        self.notification_repo = NotificationRepo()
        self.react_article_repo = ReactArticleRepo()
        self.read_article_history_repo = ReadArticleHistoryRepo()

    def save_articles(self, articles):
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
                        existing_mapping = self.mapping_repo.get_category_article_mapping(category_id, article_id)
                        if not existing_mapping:
                            self.mapping_repo.create_category_article_mapping(category_id, article_id)

            is_latest = self.article_repo.get_latest_status(article_id)[0][0]
            if is_latest:
                self.notification_repo.insert_notifications_for_article(article_id)

            self.article_repo.update_latest_status(article_id)

    def save_article_read_history(self, article_id: int, user_id: int):
        existing_article_read_history = self.read_article_history_repo.get_article_read_history(user_id, article_id)
        if existing_article_read_history:
            self.read_article_history_repo.update_article_read_date(user_id, article_id)
        else:
            self.read_article_history_repo.insert_article_read_history(user_id, article_id)

    def get_articles_for_today(self, user_id):
        articles =  self.article_repo.fetch_articles_by_today(user_id)
        if not articles:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Articles not found")
        read_history = [self.save_article_read_history(article[0], user_id) for article in articles]
        if not read_history:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Won't read the articles")
        return articles

    def get_articles_by_date_range(self, user_id, start_date, end_date, category):
        articles =  self.article_repo.fetch_articles_by_date_range(user_id, start_date, end_date, category)
        if not articles:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Articles not found")
        read_history = [self.save_article_read_history(article[0], user_id) for article in articles]
        if not read_history:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Won't read the articles")
        return articles

    def search_articles_by_keyword(self, start_date, end_date, keyword, sort_by,  user_id):
        articles = self.article_repo.search_articles(start_date, end_date, keyword, sort_by, user_id)
        if not articles:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Articles not found")
        read_history = [self.save_article_read_history(article[0], user_id) for article in articles]
        if not read_history:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Won't read the articles")
        return articles

    def save_article(self, user_id, article_id):
        existing_article = self.article_repo.find_save_article(user_id, article_id)
        if existing_article:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Article already saved")

        if self.article_repo.save_article(user_id, article_id):
            return {"message": "Article saved successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article already saved")

    def get_saved_articles(self, user_id):
        return self.article_repo.get_saved_articles(user_id)

    def get_liked_articles(self, user_id):
        return self.article_repo.get_liked_articles(user_id)

    def delete_saved_article(self, user_id, article_id):
        return self.article_repo.delete_saved_article(user_id, article_id)

    def react_to_article(self, user_id: int, article_id: int, is_like:bool):
        existing_reaction = self.react_article_repo.get_reaction(user_id, article_id)
        if existing_reaction:
             if not self.react_article_repo.update_reaction(user_id, article_id, is_like):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Won't be able to react")
        else:
            if self.react_article_repo.insert_reaction(user_id, article_id, is_like):
                pass
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Won't be able to react")

        self.article_repo.update_likes_dislikes()
        return {"message": "You reacted on an article"}


    def submit_article_report(self, article_id: int, user_id: int, reason: str):
        existing_reaction = self.report_article_repo.get_article_report(article_id, user_id)
        if existing_reaction:
            self.report_article_repo.update_article_report(article_id, user_id, reason)
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Article already reported")
        else:
            if self.report_article_repo.insert_article_report(article_id, user_id, reason):
                return {"message": "Article reported successfully"}
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Won't be able to report")

    def check_article_report(self):
        reports = self.report_article_repo.get_all_reported_articles()
        return reports

    def hide_article_report(self, article_id):
        report = self.report_article_repo.count_reports_for_article(article_id)
        if not report:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Article with id {article_id} doesn't exist")
        article_id = report[0][0]
        report_count = report[0][1]
        if report_count >= int(os.getenv("REPORT_THRESHOLD")):
            self.article_repo.set_article_hidden(article_id, True)
        return {"message": f"Article hidden successfully"}

    def hide_reported_articles_with_keyword(self, keyword):
        keyword = keyword.strip()
        if not keyword:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Keyword not found")
        articles = self.article_repo.search_articles_with_keyword(keyword)
        if not articles:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Articles not found with the keyword name {keyword}")
        for article in articles:
            article_id = article[0]
            self.article_repo.set_article_hidden(article_id, True)
        return {"message": f"Article hidden successfully"}

    def hide_articles_by_category(self, category_name: str):
        category = self.category_repo.find_category(category_name)
        if category:
            category_id, category_name = category[0]
            updated_rows = self.article_repo.set_articles_hidden_by_category(category_id)
            return {"message": f"{updated_rows} articles from category {category_id} were hidden successfully."}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Category not found")




