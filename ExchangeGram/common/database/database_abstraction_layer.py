from typing import List
from common.models.User import User
from common.models.Post import Post
from common.models.Comment import Comment
from common.password_hashing import *
from common.database.abstract_database import AbstractDatabase
from datetime import datetime


class Dbal:
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def register(self, username: str, email: str, password: str) -> User:
        new_user = self.db.create_user(
            User(
                username=username,
                email=email,
                password_hash=gen_pwd_hsh(password),
            )
        )
        if new_user is None:
            raise Exception("Could not Create User")
        return new_user

    def add_post(self, user_id: int, content: str) -> Post:
        new_post = self.db.create_post(
            Post(
                user_id=user_id,
                content=content,
                date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            )
        )
        if new_post is None:
            raise Exception("Could not Create User")
        return new_post

    def add_comment(self, post_id: int, user_id: int, content: str) -> Comment:
        new_comment = self.db.create_comment(
            Comment(
                post_id=post_id,
                user_id=user_id,
                content=content,
                date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            )
        )
        if new_comment is None:
            raise Exception("Could not Create Comment")
        return new_comment

    def authenticate(self, username: str, password: str) -> User:
        user = self.db.get_user_by_username(username)
        if user == None:
            return False
        if (
            check_pwd(password.encode("utf-8"), user._password_hash.encode("utf-8"))
            == False
        ):
            return False
        return user
