from NewsAggregationSystem.server.database import db_query

class KeywordRepo:
    def find_or_create_keyword(self, keyword):
        result = db_query("SELECT * FROM keyword WHERE keyword_name = %s", (keyword,))
        if result:
            return True, result
        else:
            db_query("INSERT INTO keyword (keyword_name) VALUES (%s)", (keyword,))
            return False, None

    def find_latest_keyword(self, ):
        result = db_query("SELECT * FROM keyword order by keyword_id desc limit 1", ())
        return result[0]


