import os
import mysql.connector
from mysql.connector import Error

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
            print("Times Won = ", row[3])
            print("Image Location =", row[4])

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


def uregsiter(userId, userName):
    try:
        print("\nChecking for user with id " + str(userId))
        connection = mysql.connector.connect(host=os.environ['DB_HOST'],
                                             database=os.environ['DB_NAME'],
                                             user=os.environ['DB_USER'],
                                             password=os.environ['DB_PASS'])

        Query = "Select * from player p where p.id = %s or p.user_name = %s"
        cursor = connection.cursor()
        cursor.execute(Query, (userId, userName,))
        records = cursor.fetchall()
        users = records
        print("Total number of rows in player: ", cursor.rowcount)

        for row in records:
            print("ID = ", row[0])
            print("User Name = ", row[1])
            print("Score = ", row[2])
            print("Active Games = ", row[3], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

        return users


def iuser(userId, userName):
    try:

        print("\nInserting new user with id " + str(userId) + " and User Name " + userName)
        connection = mysql.connector.connect(host=os.environ['DB_HOST'],
                                             database=os.environ['DB_NAME'],
                                             user=os.environ['DB_USER'],
                                             password=os.environ['DB_PASS'])

        Query = "INSERT INTO player (id, user_name) VALUES (%s, %s)"
        cursor = connection.cursor()
        cursor.execute(Query, (userId, userName,))


    except Error as e:
        print("Error inserting data to MySQL table", e)

    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
