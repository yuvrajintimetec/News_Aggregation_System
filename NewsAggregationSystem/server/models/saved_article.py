from NewsAggregationSystem.server.database import db_query

create_saved_article_table_query = """
CREATE TABLE saved_article (
    saved_article_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    article_id INT NOT NULL,
    saved_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES user(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (article_id) REFERENCES article(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

result = db_query(create_saved_article_table_query)

if result is not None:
    print("Table created successfully.")

