from fastapi.params import Depends, Query, Body
from NewsAggregationSystem.server.dtos.responses.notification_details_response import NotificationDetailsResponse
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user
from NewsAggregationSystem.server.controllers.user_controller import UserController
from fastapi import APIRouter
from datetime import date
from NewsAggregationSystem.server.dtos.requests.notification_configuration_request import NotificationConfigurationRequest
from NewsAggregationSystem.server.dtos.requests.react_article_request import ReactArticleRequest
from NewsAggregationSystem.server.dtos.responses.user_detail_response import UserDetailsResponse
from NewsAggregationSystem.server.dtos.responses.article_details_response import ArticleDetailsResponse
from NewsAggregationSystem.server.dtos.responses.save_atrticle_response import SaveArticleResponse
from NewsAggregationSystem.server.dtos.responses.delete_article_response import DeleteArticleResponse
from NewsAggregationSystem.server.dtos.requests.report_article_request import ReportArticleRequest

router = APIRouter(prefix="/api/user")
user_controller = UserController()

@router.get("/profile", response_model=UserDetailsResponse)
def get_user_profile(user_info=Depends(get_current_user)):
    return user_controller.get_user_by_id(user_info["user_id"])


@router.get("/headlines/today", response_model=ArticleDetailsResponse)
def get_today_headlines(user_info=Depends(get_current_user)):
    return user_controller.get_today_articles(user_info)


@router.get("/headlines/range", response_model=ArticleDetailsResponse)
def get_articles_by_date_range(
    start_date: date = Query(...),
    end_date: date = Query(...),
    category: str = Query("all"),
    user_info=Depends(get_current_user)
):
    return user_controller.get_articles_by_range(user_info, start_date, end_date, category)


@router.post("/saved-article/{article_id}", response_model=SaveArticleResponse)
def save_article(article_id: int, user_info=Depends(get_current_user)):
    return user_controller.save_article_for_user(user_info, article_id)


@router.get("/saved-articles", response_model=ArticleDetailsResponse)
def get_saved_articles(user_info=Depends(get_current_user)):
    return user_controller.get_saved_articles(user_info)

@router.get("/liked", response_model=ArticleDetailsResponse)
def get_liked_articles(user_info=Depends(get_current_user)):
    return user_controller.get_liked_articles(user_info)


@router.delete("/saved-article/{article_id}", response_model=DeleteArticleResponse)
def delete_saved_article(article_id: int, user_info=Depends(get_current_user)):
    return user_controller.delete_saved_article(user_info, article_id)


@router.get("/articles/search", response_model=ArticleDetailsResponse)
def search_articles( start_date: date = Query(...),
    end_date: date = Query(...),
    sort_by: str = Query("likes"),
    keyword: str = Query(...), user_info=Depends(get_current_user)):
    return user_controller.search_articles(start_date, end_date, keyword, sort_by, user_info)

@router.get("/notifications", response_model=NotificationDetailsResponse)
def view_notifications(user_info=Depends(get_current_user)):
    return user_controller.view_notifications(user_info["user_id"])

@router.post("/notifications/configure")
def configure_notifications(config: NotificationConfigurationRequest, user_info=Depends(get_current_user)):
    return user_controller.configure(user_info["user_id"], config)

@router.post("/react/{article_id}")
def react_to_article(
    article_id:int,
    react_body : ReactArticleRequest,
    user_info=Depends(get_current_user)
):
    return user_controller.react_to_article(user_info["user_id"], article_id, react_body.is_like)


@router.post("/report-article/{article_id}")
def report_article(article_id: int, report_body: ReportArticleRequest  = Body(...), current_user=Depends(get_current_user)):
    return user_controller.report_article(article_id, current_user["user_id"], report_body.reason)



