from NewsAggregationSystem.server.exceptions.category_already_exist import CategoryAlreadyExistException
from NewsAggregationSystem.server.exceptions.invalid_data_exception import InvalidDataException
from NewsAggregationSystem.server.repos.category_repo import CategoryRepo
from fastapi import HTTPException, status
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException

class CategoryService:
    def __init__(self):
        self.category_repo = CategoryRepo()

    def add_category(self, category_name: str):
        category_name = category_name.strip().lower()
        if not category_name:
            raise InvalidDataException("Category name cannot be empty")
        category = self.category_repo.find_category(category_name)
        if category:
            raise CategoryAlreadyExistException("Category already exist")
        return self.category_repo.insert_category(category_name)

    def get_all_categories(self):
        categories = self.category_repo.fetch_all_categories()
        if not categories:
            raise NotFoundException("No categories found")
        return [{"category_id": category[0], "category_name": category[1]} for category in categories]