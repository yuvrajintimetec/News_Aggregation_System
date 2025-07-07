from NewsAggregationSystem.server.database import db_query

create_keyword_table_query = """
CREATE TABLE keyword (
    keyword_id INT AUTO_INCREMENT PRIMARY KEY,
    keyword_name VARCHAR(100) NOT NULL UNIQUE
);
"""

result = db_query(create_keyword_table_query)

if result is not None:
    print("Table created successfully.")

