import mysql.connector

def get_mysql_conn():

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "schooldb"
    )

    return conn