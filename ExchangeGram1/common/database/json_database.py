# Json Database
from .abstract_database import AbstractDatabase
from typing import List
import json
import os
from common.models.user import User
from common.models.post import Post
from common.models.comment import Comment


class jsonDatabase(AbstractDatabase):
    def __init__(self, path: str) -> None:
        self._user_filepath = os.path.join(path, "user.dat")
        self._post_filepath = os.path.join(path, "post.dat")
        self._comment_filepath = os.path.join(path, "comment.dat")

        self._users = []
        self._posts = []
        self._comments = []

        self._load_data()

    def _load_data(self):
        self._load_users()
        self._load_posts()
        self._load_comments()

    def _load_users(self):
        if not os.path.exists(self._user_filepath):
            return
        with open(self._user_filepath, "r") as infile:
            data: List[dict] = json.load(infile)
            for d in data:
                user = User(
                    username=d["_username"],
                    email=d["_email"],
                    password_hash=d["_password_hash"],
                )
                user.follows = d["follows"]
                user._id = d["_id"]
                self._users.append(user)

    def _save_users(self):
        with open(self._user_filepath, "w") as outfile:
            json_string = json.dumps([u.__dict__ for u in self._users])
            outfile.write(json_string)

    def create_user(self, user: User) -> User:
        self._users.append(user)

    def delete_user(self, user: User) -> bool:
        pass

    def update_user(self, user: User) -> User:
        pass

    def _load_posts(self):
        pass

    def _save_posts(self):
        pass

    def _load_comments(self):
        pass

    def update_user(self, user: User) -> User:
        pass

    def delete_user(self, user: User) -> bool:
        pass

    def username_is_unique(self, username: str) -> bool:
        pass

    def email_is_unique(self, username: str) -> bool:
        pass

    def authenticate(self, user: User) -> User:
        pass