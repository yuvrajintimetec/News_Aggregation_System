from NewsAggregationSystem.server.database import db_query

create_article_reaction_table_query = """
CREATE TABLE article_reaction (
    reaction_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    article_id INT NOT NULL,
    is_like BOOLEAN DEFAULT FALSE,
    is_dislike BOOLEAN DEFAULT FALSE,
    reaction_date DATETIME DEFAULT NOW(),
    UNIQUE(user_id, article_id), 
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (article_id) REFERENCES article(article_id)
);
"""

result = db_query(create_article_reaction_table_query)

if result is not None:
    print("Table created successfully.")

