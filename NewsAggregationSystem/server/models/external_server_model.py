from NewsAggregationSystem.server.database import db_query

create_external_server_table_query = """
CREATE TABLE external_server (
    server_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    server_name VARCHAR(100) NOT NULL,
    api_key VARCHAR(255) NOT NULL,
    base_url VARCHAR(500) NOT NULL,
    is_active TINYINT(1) DEFAULT 1
);
"""

result = db_query(create_external_server_table_query)

if result is not None:
    print("Table created successfully.")

