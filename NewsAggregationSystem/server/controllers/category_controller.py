from NewsAggregationSystem.server.services.category_service import CategoryService

class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()

    def get_all_categories(self):
        categories = self.category_service.get_all_categories()
        return {"message": categories}
