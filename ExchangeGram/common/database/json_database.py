# Json Database
from .abstract_database import AbstractDatabase
from typing import List
import json
import os
from common.models.User import User
from common.models.Post import Post
from common.models.Comment import Comment


class jsonDatabase(AbstractDatabase):
    def __init__(self, path: str) -> None:
        self._user_filepath = os.path.join(path, "user.dat")
        self._post_filepath = os.path.join(path, "post.dat")
        self._comment_filepath = os.path.join(path, "comment.dat")

        self._users = []
        self._posts = []
        self._comments = []

        self._accumulate_user_id = 0
        self._accumulate_post_id = 0
        self._accumulate_comment_id = 0

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
                if user._id > self._accumulate_user_id:
                    self._accumulate_user_id = user._id
                self._users.append(user)

    def _save_users(self):
        with open(self._user_filepath, "w") as outfile:
            outfile.write(json.dumps([u.__dict__ for u in self._users]))

    def create_user(self, user: User) -> User:
        self._accumulate_user_id += 1
        user._id = self._accumulate_user_id
        self._users.append(user)
        self._save_users()
        return user

    def delete_user(self, user: User) -> bool:
        if user not in self._users:
            return False
        for u in self._users:
            u.follows.remove(user._id)
        self._users.remove(user)
        self._save_users()
        return True

    def update_user(self, user: User) -> User:
        pass

    def _load_posts(self):
        if not os.path.exists(self._post_filepath):
            return
        with open(self._post_filepath, "r") as infile:
            data: List[dict] = json.load(infile)
            for d in data:
                post = Post(
                    user_id=d["_user_id"],
                    content=d["content"],
                    date=d["date"],
                )
                post.views = d["views"]
                post.likes = d["likes"]
                post._id = d["_id"]
                if post._id > self._accumulate_post_id:
                    self._accumulate_post_id = post._id
                self._posts.append(post)

    def _save_posts(self):
        with open(self._post_filepath, "w") as outfile:
            outfile.write(json.dumps([p.__dict__ for p in self._posts]))

    def create_post(self, post) -> Post:
        self._accumulate_post_id += 1
        post._id = self._accumulate_post_id
        self._posts.append(post)
        self._save_posts()
        return post

    def delete_post(self, post: Post) -> bool:
        if post not in self._posts:
            return False
        for p in self._posts:
            p.remove(post)
        self._posts.remove(post)
        self._save_posts()
        return True

    def update_post(self, post: Post) -> Post:
        pass

    def _load_comments(self):
        pass

    def _save_comments(self):
        pass

    def create_comments(self, user: User) -> User:
        pass

    def delete_comments(self, user: User) -> bool:
        pass

    def update_comments(self, user: User) -> User:
        pass

    def username_is_unique(self, username: str) -> bool:
        pass

    def email_is_unique(self, username: str) -> bool:
        pass

    def authenticate(self, user: User) -> User:
        pass