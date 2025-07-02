from NewsAggregationSystem.server.database import db_query

class KeywordArticleMappingRepo:
    def create_keyword_article_mapping(self, keyword_id, article_id):
        query = '''insert into keyword_article_mapping(keyword_id, article_id) values(%s,%s)'''
        db_query(query, (keyword_id, article_id))


    def get_keyword_article_mapping(self, keyword_id: int, article_id: int):
        query = """
            SELECT * FROM keyword_article_mapping
            WHERE keyword_id = %s AND article_id = %s
        """
        return db_query(query, (keyword_id, article_id))


