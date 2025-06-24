from NewsAggregationSystem.server.database import db_query

class CategoryArticleMappingRepo:
    def create_category_article_mapping(self, category_id, article_id):
        query = '''insert into category_article_mapping(category_id, article_id) values(%s,%s)'''
        db_query(query, (category_id, article_id))


