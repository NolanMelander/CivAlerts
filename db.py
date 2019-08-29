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


def cinfo():
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


def linfo():
    try:
        connection = mysql.connector.connect(host=os.environ['DB_HOST'],
                                             database=os.environ['DB_NAME'],
                                             user=os.environ['DB_USER'],
                                             password=os.environ['DB_PASS'])
        Query = "select l.id, l.leader_name, c.civ_name, civ.civ_name, l.times_played, l.times_won " \
                "from leader l left join civilization c on l.civ_id = c.id " \
                "left join civilization civ on l.alternate_civ_id = civ.id"
        cursor = connection.cursor()
        cursor.execute(Query)
        records = cursor.fetchall()
        leader = records
        print("Total number of rows in leaders: ", cursor.rowcount)

        print("\nPrinting each Civilization")
        for row in records:
            print("ID = ", row[0])
            print("Leader = ", row[2])
            print("Times Played = ", row[3])
            print("Times Won = ", row[4], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

        return leader