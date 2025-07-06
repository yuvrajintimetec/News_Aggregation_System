from NewsAggregationSystem.server.database import db_query

class CategoryRepo:
    def find_category(self, category_name):
        category_name = category_name.strip().lower()
        query = '''Select * from category where category_name = %s'''
        return db_query(query, (category_name,))

    def insert_category(self, category_name: str):
        query = '''INSERT INTO category (category_name) VALUES (%s)'''
        return db_query(query, (category_name.lower(),))

    def fetch_all_categories(self):
        query = "SELECT category_id, category_name FROM category"
        return db_query(query)


