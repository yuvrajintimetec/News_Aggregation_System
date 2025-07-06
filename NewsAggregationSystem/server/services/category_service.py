from NewsAggregationSystem.server.repos.category_repo import CategoryRepo
from fastapi import HTTPException, status

class CategoryService:
    def __init__(self):
        self.category_repo = CategoryRepo()

    def add_category(self, category_name: str):
        return self.category_repo.insert_category(category_name)

    def get_all_categories(self):
        categories = self.category_repo.fetch_all_categories()
        if not categories:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No categories found")
        return [{"category_id": category[0], "category_name": category[1]} for category in categories]