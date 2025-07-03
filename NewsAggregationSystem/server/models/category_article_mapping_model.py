from NewsAggregationSystem.server.database import db_query

create_category_article_mapping_table_query = """
CREATE TABLE category_article_mapping (
    category_article_mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    article_id INT NOT NULL,

    FOREIGN KEY (category_id) REFERENCES category(category_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (article_id) REFERENCES article(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

result = db_query(create_category_article_mapping_table_query)

if result is not None:
    print("Table created successfully.")

