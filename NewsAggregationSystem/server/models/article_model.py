from NewsAggregationSystem.server.database import db_query

create_article_table_query = """
CREATE TABLE IF NOT EXISTS article (
    article_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    content LONGTEXT,
    source VARCHAR(255),
    url VARCHAR(500) UNIQUE,
    published_at DATETIME,
    server_id INT,
    is_hidden BOOLEAN DEFAULT FALSE,
    is_latest BOOLEAN DEFAULT TRUE,
    likes INT DEFAULT 0,
    dislikes INT DEFAULT 0,

    FOREIGN KEY (server_id) REFERENCES external_server(server_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""

result = db_query(create_article_table_query)

if result is not None:
    print("Table created successfully.")

