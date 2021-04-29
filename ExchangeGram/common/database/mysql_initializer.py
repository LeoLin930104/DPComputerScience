import mysql.connector

sql = [
    "CREATE DATABASE exchangegram",
    "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password_hash VARCHAR(255), email VARCHAR(255), follows INT) ENGINE = InnoDB;",
    "CREATE TABLE posts (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, content VARCHAR(511)) ENGINE = InnoDB;",
    "CREATE TABLE comments (post_id INT, user_id INT, content VARCHAR(511)) ENGINE = InnoDB;",
    "CREATE TABLE follows (follower INT, followee INT)",
]


def create_mysql_db(host: str, user: str, password: str, database: str):
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()
    for s in sql:
        cursor.execute(s)
        connection.commit()
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    return connection