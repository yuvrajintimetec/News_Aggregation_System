from NewsAggregationSystem.server.database import db_query

create_reported_article_table_query = """
CREATE TABLE reported_article (
    reported_article_id INT AUTO_INCREMENT PRIMARY KEY,
    article_id INT NOT NULL,
    user_id INT NOT NULL,
    report_reason TEXT,
    reported_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (article_id) REFERENCES article(article_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
"""

result = db_query(create_reported_article_table_query)

if result is not None:
    print("Table created successfully.")

