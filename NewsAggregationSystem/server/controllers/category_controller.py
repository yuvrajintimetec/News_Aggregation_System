from fastapi import Depends
from server.services.category_service import CategoryService


class CategoryController:

    def __init__(self):
      self.category_service = CategoryService()

    def add_category(self, category):
        return self.category_service.add_category(category.category_name)

