import os
import mysql.connector
from mysql.connector import Error

def db_connect():

    try:
        connection = mysql.connector.connect(host=os.environ['DB_HOST'],
                                             database=os.environ['DB_NAME'],
                                             user=os.environ['DB_USER'],
                                             password=os.environ['DB_PASS'])
        if connection.is_connected():
            info = connection.get_server_info()
            print("Connected to MySQL Server version ", info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    pass


db_connect()
