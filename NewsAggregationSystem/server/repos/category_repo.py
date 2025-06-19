from server.database import db_query

class CategoryRepo:
    def find_category(self, category_name):
        query = '''Select * from category where category_name = %s'''
        return db_query(query, (category_name,))

    def insert_category(self, category_name: str):
        query = '''INSERT INTO category (category_name) VALUES (%s)'''
        return db_query(query, (category_name,))


