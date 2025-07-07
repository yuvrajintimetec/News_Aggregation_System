from NewsAggregationSystem.server.database import db_query

create_read_article_history_table_query = """
CREATE TABLE read_article_history (
    article_history_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    article_id INT NOT NULL,
    article_read_date DATETIME DEFAULT NOW(),
    UNIQUE(user_id, article_id), 
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (article_id) REFERENCES article(article_id)
);
"""

result = db_query(create_read_article_history_table_query)

if result is not None:
    print("Table created successfully.")

