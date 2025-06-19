from fastapi import APIRouter
from server.controllers.category_controller import CategoryController
from server.dtos.requests.create_category_request import CreateCategoryRequest

router = APIRouter(prefix="/api/category")
category_controller = CategoryController()

@router.post("/")
async def add_category(category: CreateCategoryRequest):
    return category_controller.add_category(category)


