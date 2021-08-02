
    def query_popular_tickets(self,connection):

        sql_statement = """
                WITH top_selling_tickets
                AS (SELECT
                    event_name,
                    ROW_NUMBER() OVER (
                        ORDER BY num_tickets DESC) row_num
                    FROM
                    ticket_sales
                )
                SELECT
                   event_name
                FROM
                top_selling_tickets
                WHERE row_num <= 3;"""
        cursor = connection.cursor()
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        cursor.close()
        return records
