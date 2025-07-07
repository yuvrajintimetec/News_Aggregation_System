from NewsAggregationSystem.server.database import db_query

create_category_table_query = """
CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);
"""

result = db_query(create_category_table_query)

if result is not None:
    print("Table created successfully.")

