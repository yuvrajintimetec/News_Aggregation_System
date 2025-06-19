import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from server.database import db_query

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
