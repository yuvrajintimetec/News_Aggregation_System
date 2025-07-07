from NewsAggregationSystem.server.database import db_query

create_user_table_query = """
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);
"""

result = db_query(create_user_table_query)

if result is not None:
    print("Table created successfully.")

