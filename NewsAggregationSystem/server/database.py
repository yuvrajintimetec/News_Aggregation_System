import mysql.connector as sql

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
            with connection.cursor() as cursor:
                cursor.execute(query, params or ())

                if query.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()

                connection.commit()
                return cursor.rowcount

    except sql.Error as e:
        print(f"Database error: {e}")
        return None
