from NewsAggregationSystem.server.database import db_query

class UserRepo:
    def insert_user(self, name, email, password, role):
        query = '''INSERT INTO user (name, email, password, role) 
                   VALUES (%s, %s, %s, %s)'''
        db_query(query, (name, email, password, role))
        return {
                "message": "User registration successfully"
        }


    def get_user_by_email(self, email):
        query = "SELECT user_id, name, email, password, role FROM user WHERE email = %s"
        return db_query(query, (email,))

    def get_user_by_id(self, user_id):
        query = """
            SELECT user_id, name, email, role
            FROM user
            WHERE user_id = %s
        """
        return db_query(query, (user_id,))[0]

