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
        fields = []
        values = []

        for key, value in external_server_data.items():
            fields.append(f"{key} = %s")
            values.append(value)

        values.append(server_id)

        query = f"""
               UPDATE external_server
               SET {', '.join(fields)}
               WHERE server_id = %s
           """
        return db_query(query, tuple(values))

