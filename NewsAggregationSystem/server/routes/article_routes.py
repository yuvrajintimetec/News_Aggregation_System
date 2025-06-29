from fastapi import APIRouter, Depends, Query
from NewsAggregationSystem.server.controllers.article_controller import ArticleController


router = APIRouter(prefix="/api/articles")
article_controller = ArticleController()

@router.get("/external_source")
async def store_fetched_article():
        return article_controller.fetch_and_store_all_articles()






