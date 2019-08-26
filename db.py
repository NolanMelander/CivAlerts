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

def db_test():
    try:
        connection = mysql.connector.connect(host=os.environ['DB_HOST'],
                                             database=os.environ['DB_NAME'],
                                             user=os.environ['DB_USER'],
                                             password=os.environ['DB_PASS'])
        Query = "select * from civilization"
        cursor = connection.cursor()
        cursor.execute(Query)
        records = cursor.fetchall()
        civ = records
        print("Total number of rows in Civilization: ", cursor.rowcount)

        print("\nPrinting each Civilization")
        for row in records:
            print("ID = ", row[0])
            print("Civilization = ", row[1])
            print("Times Played = ", row[2])
            print("Times Won = ", row[3], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

        return civ

