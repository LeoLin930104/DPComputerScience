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
            self.cursor = self.connection.cursor()
            print(f"Connection Built to: {database}")
        except:
            raise Exception(f"Failed to Reach Connection to Database: {database}")

    def create_user(self, user: User) -> User:
        sql = "INSERT INTO users (id, username, password_hash, email) VALUES (%s, %s, %s, %s);"
        val = (0, user._username, user._password_hash, user._email)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            return
        return user

    def delete_user(self, user: User) -> bool:
        sql = "DELETE from users where id = %s RETURNING id;"
        val = user._id
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not Delete User(id: {user._id})")
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
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not Update User(id: {user._id})")
        else:
            print(f"Successfully Update User(id = {resultset})")
            self.connection.commit()
        return user

    def create_post(self, post: Post) -> Post:
        sql = "INSERT INTO users (id, user_id, content, date, views, likes) VALUES (%s, %s, %s, %s, %s, %s);"
        val = (0, post._user_id, post.date, post.content, post.views, post.likes)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            return
        return post

    def delete_post(self, post: Post) -> bool:
        sql = "DELETE from posts where id = %s RETURNING id;"
        val = post._id
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not delete Post(id: {post._id})")
        else:
            print(f"Successfully Delete Post(id = {resultset})")
            self.connection.commit()
        return True

    def update_post(self, post: Post) -> Post:
        sql = "UPDATE posts SET user_id = %s, content = %s, date = %s, views = %s, likes = %s WHERE id = %s;"
        val = (post._user_id, post.content, post.date, post.views, post.likes, post._id)
        self.cursor.ececute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not Update Post(id: {post._id})")
        else:
            print(f"Successfully Update Post(id = {resultset})")
            self.connection.commit()
        return post

    def create_comment(self, comment: Comment) -> Comment:
        sql = "INSERT INTO comments (id, user_id, post_id content, date, likes) VALUES (%s, %s, %s, %s, %s, %s);"
        val = (
            0,
            comment._user_id,
            comment._post_id,
            comment.date,
            comment.content,
            comment.likes,
        )
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            return
        return comment

    def delete_comment(self, comment: Comment) -> bool:
        sql = "DELETE from comments where id = %s RETURNING id;"
        val = comment._id
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not delete Comment(id: {comment._id})")
        else:
            print(f"Successfully Delete Comment(id = {resultset})")
            self.connection.commit()
        return True

    def update_comment(self, comment: Comment) -> Comment:
        sql = "UPDATE comments SET user_id = %s, post_id = %s, content = %s, date = %s, likes = %s WHERE id = %s;"
        val = (
            comment._user_id,
            comment._post_id,
            comment.content,
            comment.date,
            comment.likes,
            comment._id,
        )
        self.cursor.ececute(sql, val)
        resultset = self.cursor.fetchall()
        if resultset is None:
            raise Exception(f"Could not Update Comment(id: {comment._id})")
        else:
            print(f"Successfully Update Comment(id = {resultset})")
            self.connection.commit()
        return comment

    def username_is_unique(self, username: str) -> bool:
        sql = "SELECT * FROM users WHERE username = %s"
        val = (username,)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            return False
        else:
            return True

    def email_is_unique(self, email: str) -> bool:
        sql = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            return False
        else:
            return True

    # Search for User from Username
    def get_user_by_username(self, username: str) -> User:
        sql = "SELECT * FROM users WHERE username = %s"
        val = (username,)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            user = User(
                username=resultset[0][1],
                password_hash=resultset[0][2],
                email=resultset[0][3],
            )
            user._id = resultset[0][0]
            return user
        return

    # Search for User from Email
    def get_user_by_email(self, email: str) -> User:
        sql = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        resultset = self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            user = User(
                username=resultset[0][1],
                password_hash=resultset[0][2],
                email=resultset[0][3],
            )
            user._id = resultset[0]
            return user
        return
