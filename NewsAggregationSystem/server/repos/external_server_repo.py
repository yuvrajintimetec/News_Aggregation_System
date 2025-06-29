from NewsAggregationSystem.server.database import db_query

class ExternalServerRepo:

    def update_last_accessed(self, server_id):
        query = '''UPDATE external_server SET last_accessed = NOW()  WHERE server_id = %s'''
        return db_query(query, (server_id,))


    def get_all_servers(self):
        query = '''SELECT * FROM external_server'''
        return db_query(query)

    def get_active_servers(self):
        query = '''SELECT * FROM external_server where is_active=1'''
        return db_query(query)

    def update_server(self, server_id, external_server_data):
        print(external_server_data)
        query = '''Update external_server SET api_key = %s WHERE server_id = %s'''
        return db_query(query, (external_server_data['api_key'], server_id))

