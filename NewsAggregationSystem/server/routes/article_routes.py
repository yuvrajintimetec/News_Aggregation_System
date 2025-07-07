from fastapi import APIRouter, Depends, Query
from NewsAggregationSystem.server.controllers.article_controller import ArticleController
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user

router = APIRouter(prefix="/api/articles")
article_controller = ArticleController()

@router.get("/external_source")
async def store_fetched_article():
        return article_controller.fetch_and_store_all_articles()

@router.get("/{article_id}")
def get_article(article_id: int, user_info=Depends(get_current_user)):
    return article_controller.get_article(user_info, article_id)






