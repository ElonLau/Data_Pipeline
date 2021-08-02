
    def load_third_party(self,connection, file_path_csv):

        cursor = connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS ticket_sales""")

        cursor.execute("""
            CREATE TABLE ticket_sales(
                    ticket_id INT,
                    trans_date DATE,
                    event_id INT,
                    event_name VARCHAR(50),
                    event_date DATE,
                    event_type VARCHAR(10),
                    event_city VARCHAR(20),
                    customer_id INT,
                    price DECIMAL(10,2),
                    num_tickets INT
                    );
           """
           )
        f = open(file_path_csv,"r")
        dt = reader(f)
        sql = """INSERT INTO ticket_sales VALUES(%s,%s,%s);"""
        for row in dt:
            cursor.execute(sql, tuple(row))
        connection.commit()
        cursor.close()
