from server.repos.category_repo import CategoryRepo

class CategoryService:
    def __init__(self):
        self.category_repo = CategoryRepo()

    def add_category(self, category_name: str):
        return self.category_repo.insert_category(category_name)
