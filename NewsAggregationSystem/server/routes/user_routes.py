from fastapi.params import Depends, Query
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user
from NewsAggregationSystem.server.controllers.user_controller import UserController
from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix="/api/user")
user_controller = UserController()

@router.get("/profile")
def get_user_profile(user_info=Depends(get_current_user)):
    user = user_controller.get_user_by_id(user_info["user_id"])[0]
    print(user)
    return {
        "user_id":user[0],
        "name":user[1],
        "email":user[2],
        "user_role":user[3]
    }

@router.get("/headlines/today")
def get_today_headlines(user_info=Depends(get_current_user)):
    return user_controller.get_today_articles(user_info)


@router.get("/headlines/range")
def get_articles_by_date_range(
    start_date: date = Query(...),
    end_date: date = Query(...),
    category: str = Query(...),
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
def search_articles( start_date: date = Query(...),
    end_date: date = Query(...),
    keyword: str = Query(...), user_info=Depends(get_current_user)):
    return user_controller.search_articles(start_date, end_date, keyword, user_info)




