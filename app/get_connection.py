import mysql.connector

def get_mysql_conn():

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "thanos888",
        database = "schooldb"
    )

    return conn