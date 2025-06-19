from fastapi.params import Depends, Query
from server.middleware.authentication_middleware import get_current_user
from server.controllers.user_controller import UserController
from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix="/api/user")
user_controller = UserController()

@router.get("/profile")
async def get_user_profile(user_info = Depends(get_current_user)):
    return user_info

@router.get("/headlines/today")
def get_today_headlines(user_info=Depends(get_current_user)):
    return user_controller.get_today_articles(user_info)


@router.get("/headlines/range")
def get_articles_by_date_range(
    start_date: date = Query(...),
    end_date: date = Query(...),
    category: str = Query("all"),
    user_info=Depends(get_current_user)
):
    return user_controller.get_articles_by_range(user_info, start_date, end_date, category)


@router.post("/save/{article_id}")
def save_article(article_id: int, user_info=Depends(get_current_user)):
    return user_controller.save_article_for_user(user_info, article_id)


@router.get("/saved")
def get_saved_articles(user_info=Depends(get_current_user)):
    return user_controller.get_saved_articles(user_info)


@router.delete("/saved/{article_id}")
def delete_saved_article(article_id: int, user_info=Depends(get_current_user)):
    return user_controller.delete_saved_article(user_info, article_id)


@router.get("/search")
def search_articles(keyword: str = Query(...), user_info=Depends(get_current_user)):
    return user_controller.search_articles(keyword, user_info)




