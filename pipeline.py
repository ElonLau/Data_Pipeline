import logging
import mysql.connector
from mysql.connector import Error
import csv
from csv import reader
import get_db_connection
import load_third_party
import query_popular_tickets


config = configparser.ConfigParser()
config.read('database.cfg')


class DataPipeline(object):

    def __init__(self):
        self.username=config['DATABASE']['DB_USER']
        self.password=config['DATABASE']['DB_PASSWORD']
        self.host=config['DATABASE']['DB_HOST']
        self.port=config['DATABASE']['DB_PORT']
        self.database=config['DATABASE']['DATABASE']


if __name__ == "__main__":
    dp=DataPipeline()
    connection=dp.get_db_connection()
    dp.load_third_party(connection,"third_party_sales_1.csv")
    records=dp.query_popular_tickets(connection)
    print("Here are the most popular tickets in the past month: ")
    for rec in records:
        print("- ",rec[0])
