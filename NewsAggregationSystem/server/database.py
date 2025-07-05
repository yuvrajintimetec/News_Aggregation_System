import mysql.connector as sql
from fastapi import HTTPException

def get_connection():
    return sql.connect(
        host= "localhost",
        user="root",
        passwd="123456",
        database= "news_aggregation",
        auth_plugin="mysql_native_password"
    )


def db_query(query, params=None):
    try:
        connection = get_connection()
        with connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(query, params or ())

                if query.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()

                connection.commit()
                return cursor.rowcount

    except sql.Error as error:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {error}"
        )
