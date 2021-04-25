import mysql.connector


def create_mysql_db(host: str, user: str, password: str, database: str):
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE exchangegram")
    cursor.execute(
        "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password_hash VARCHAR(255), email VARCHAR(255), follows INT) ENGINE = InnoDB;"
    )
    cursor.execute(
        "CREATE TABLE posts (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, content VARCHAR(511)) ENGINE = InnoDB;"
    )
    cursor.execute(
        "CREATE TABLE comments (post_id INT, user_id INT, content VARCHAR(511)) ENGINE = InnoDB;"
    )
    connection.commit()
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    return connection