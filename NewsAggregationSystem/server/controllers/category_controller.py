from NewsAggregationSystem.server.services.category_service import CategoryService
from fastapi import HTTPException, status
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException

class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()

    def get_all_categories(self):
        try:
            categories = self.category_service.get_all_categories()
            return {"message": categories}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
