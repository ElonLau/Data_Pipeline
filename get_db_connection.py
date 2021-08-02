def get_db_connection(self):


      connection = None
      try:
          connection = mysql.connector.connect(user=self.username,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)
      except Exception as error:
          print("Error while connecting to database", error)

      return connection
