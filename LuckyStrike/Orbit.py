import mysql.connector


def connectTo(hostname, username, user_password, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            passwd = user_password,
            database = dbname
        )
        print("Connected to MySQL Database: " + dbname)
    except Error as err:
        print("Cannot Connect")

    return connection


connection = connectTo('localhost','root','password','luckystrike')

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print("Cannot Execute")

def readQuery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print("Cannot Read")

