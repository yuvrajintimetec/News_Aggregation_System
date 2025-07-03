from NewsAggregationSystem.server.database import db_query

create_notification_setting_table_query = """
CREATE TABLE notification_setting (
    notification_setting_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT,
    keyword_id INT,
    is_enabled BOOLEAN,
    
	FOREIGN KEY (keyword_id) REFERENCES keyword(keyword_id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
        
	FOREIGN KEY (category_id) REFERENCES category(category_id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
    
    FOREIGN KEY (user_id) REFERENCES user(user_id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);
"""

result = db_query(create_notification_setting_table_query)

if result is not None:
    print("Table created successfully.")

