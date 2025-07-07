from fastapi import APIRouter, Depends
from NewsAggregationSystem.server.controllers.category_controller import CategoryController
from NewsAggregationSystem.server.dtos.responses.category_details_response import CategoryDetailsResponse
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user

router = APIRouter(prefix="/api/category")
category_controller = CategoryController()

@router.get("/", response_model=CategoryDetailsResponse)
def get_all_categories(user_info=Depends(get_current_user)):
    return category_controller.get_all_categories()
