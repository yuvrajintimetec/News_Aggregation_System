from NewsAggregationSystem.server.database import db_query

create_notification_table_query = """
CREATE TABLE notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    notification_setting_id INT,
    article_id INT NOT NULL,
    message TEXT,
    notification_date DATETIME,
    is_read BOOLEAN DEFAULT FALSE,
    
    FOREIGN KEY (user_id) REFERENCES user(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (article_id) REFERENCES article(article_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	
    FOREIGN KEY (notification_setting_id) REFERENCES notification_setting(notification_setting_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

result = db_query(create_notification_table_query)

if result is not None:
    print("Table created successfully.")

