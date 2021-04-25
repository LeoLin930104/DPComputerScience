# MySQL Database
import mysql.connector
from common.database.abstract_database import AbstractDatabase
from common.database.mysql_initializer import create_mysql_db
from common.models.User import User
from common.models.Post import Post
from common.models.Comment import Comment


class mysqlDatabase(AbstractDatabase):
    def __init__(self, host: str, username: str, password: str, database: str):
        try:
            self.connection = mysql.connector.connect(
                host=host, user=username, password=password, database=database
            )
        except:
            self.connection = create_mysql_db(
                host=host, user=username, password=password, database=database
            )
        self.cursor = self.connection.cursor()

    def create_user(self, user: User) -> User:
        sql = "INSERT INTO users (id, username, password_hash, email) VALUES (%s, %s, %s, %s); ALTER TABLE follows ADD %s INT(10);"
        val = (0, user._username, user._password_hash, user._email.user._username)
        self.cursor.execute(sql, val)
        sql = f""
        self.cursor.execute(sql)
        self.connection.commit()
        return user

    def delete_user(self, user: User) -> bool:
        sql = "DELETE from users where id = %s RETURNING id;"
        val = user._id
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not delete User(id: {user._id})")
        else:
            print(f"Successfully Delete User(id = {resultset})")
            self.connection.commit()
        return True

    def update_user(self, user: User) -> User:
        sql = (
            "UPDATE users SET username= %s, password_hash= %s, email= %s WHERE id = %s;"
        )
        val = (user._username, user._password_hash, user._email, user._id)
        self.cursor.ececute(sql, val)
        for f in user.follows:
            sql = "INSERT INTO follows "
        self.connection.commit()
        return user

    def username_is_unique(self, username: str) -> bool:
        pass

    def email_is_unique(self, username: str) -> bool:
        pass

    # Search for User from Username
    def get_user_by_username(self, username: str) -> User:
        pass

    # Search for User from Email
    def get_user_by_email(self, email: str) -> User:
        pass
