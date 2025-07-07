from NewsAggregationSystem.server.database import db_query

create_keyword_article_mapping_table_query = """
CREATE TABLE keyword_article_mapping (
    keyword_article_mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    keyword_id INT,
    article_id INT NOT NULL,

    FOREIGN KEY (keyword_id) REFERENCES keyword(keyword_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (article_id) REFERENCES article(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

result = db_query(create_keyword_article_mapping_table_query)

if result is not None:
    print("Table created successfully.")

