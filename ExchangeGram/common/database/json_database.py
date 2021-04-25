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

    # Caller of Loading data from user.dat, post.dat, comment.dat
    def _load_data(self):
        self._load_users()
        self._load_posts()
        self._load_comments()

    # Load data from user.dat
    def _load_users(self):
        if not os.path.exists(self._user_filepath):
            return
        with open(self._user_filepath, "r") as infile:
            data: List[dict] = None
            try:
                data = json.load(infile)
            except Exception as err:
                print("user.dat: File was Empty")
                return
            for d in data:
                user = User(
                    username=d["_username"],
                    email=d["_email"],
                    password_hash=d["_password_hash"],
                )
                user._id = d["_id"]
                user.follows = d["follows"]
                if user._id > self._accumulate_user_id:
                    self._accumulate_user_id = user._id
                self._users.append(user)
        print("user.dat: File Loaded")

    # Writes users data back into user.dat
    def _save_users(self):
        with open(self._user_filepath, "w") as outfile:
            outfile.write(json.dumps([u.__dict__ for u in self._users]))

    # Append new user into users
    def create_user(self, user: User) -> User:
        self._accumulate_user_id += 1
        user._id = self._accumulate_user_id
        self._users.append(user)
        self._save_users()
        return user

    # Remove specific user from users
    def delete_user(self, user: User) -> bool:
        if user not in self._users:
            return False
        for u in self._users:
            u.follows.remove(user._id)
        self._users.remove(user)
        self._save_users()
        return True

    # Replace specific user with updated data
    def update_user(self, user: User) -> User:
        idx = 0
        contains = False
        for u in self._users:
            if u._id == user._id:
                self._users[idx] = user
                contains = True
                break
            idx += 1
        if contains == False:
            return
        self._save_users()
        return user

    # Load data from post.dat
    def _load_posts(self):
        if not os.path.exists(self._post_filepath):
            return
        with open(self._post_filepath, "r") as infile:
            data: List[dict] = None
            try:
                data = json.load(infile)
            except Exception as err:
                print("post.dat: File was Empty")
                return
            for d in data:
                post = Post(
                    user_id=d["_user_id"],
                    content=d["content"],
                    date=d["date"],
                )
                post._id = d["_id"]
                post.likes = d["likes"]
                post.views = d["views"]
                if post._id > self._accumulate_post_id:
                    self._accumulate_post_id = post._id
                self._posts.append(post)
        print("post.dat: File Loaded")

    # Writes posts data back into post.dat
    def _save_posts(self):
        with open(self._post_filepath, "w") as outfile:
            outfile.write(json.dumps([p.__dict__ for p in self._posts]))

    # Append new post into posts
    def create_post(self, post) -> Post:
        self._accumulate_post_id += 1
        post._id = self._accumulate_post_id
        self._posts.append(post)
        self._save_posts()
        return post

    # Remove specific post from posts
    def delete_post(self, post: Post) -> bool:
        if post not in self._posts:
            return False
        for p in self._posts:
            p.remove(post)
        self._posts.remove(post)
        self._save_posts()
        return True

    # Replace specific post with updated data
    def update_post(self, post: Post) -> Post:
        idx = 0
        contains = False
        for p in self._posts:
            if p._id == post._id:
                self._posts[idx] = post
                contains = True
                break
            idx += 1
        if contains == False:
            return
        self._save_posts()
        return post

    # Load data from comment.dat
    def _load_comments(self):
        if not os.path.exists(self._comment_filepath):
            return
        with open(self._comment_filepath, "r") as infile:
            data: List[dict] = None
            try:
                data = json.load(infile)
            except Exception as err:
                print("comment.dat: File was Empty")
                return
            for d in data:
                comment = Comment(
                    post_id=d["_post_id"],
                    user_id=d["_user_id"],
                    content=d["content"],
                    date=d["date"],
                )
                comment._id = d["_id"]
                comment.likes = d["likes"]
                if comment._id > self._accumulate_comment_id:
                    self._accumulate_comment_id = comment._id
                self._comments.append(comment)
        print("comment.dat: File Loaded")

    # Writes comments data back into comment.dat
    def _save_comments(self):
        with open(self._comment_filepath, "w") as outfile:
            outfile.write(json.dumps([c.__dict__ for c in self._comments]))

    # Append new comment into comments
    def create_comment(self, comment: Comment) -> Comment:
        self._accumulate_comment_id += 1
        comment._id = self._accumulate_comment_id
        self._comments.append(comment)
        self._save_comments()
        return comment

    # Remove specific comment from comments
    def delete_comment(self, comment: Comment) -> bool:
        if comment not in self._comment:
            return False
        for c in self._comment:
            c.remove(comment)
        self._comment.remove(comment)
        self._save_comments()
        return True

    # Replace specific comment with updated data
    def update_comment(self, comment: Comment) -> Comment:
        idx = 0
        contains = False
        for c in self._posts:
            if c._id == comment._id:
                self._comments[idx] = comment
                contains = True
                break
            idx += 1
        if contains == False:
            return
        self._save_comments()
        return comment

    # Check for if username is unique
    def username_is_unique(self, username: str) -> bool:
        for u in self._users:
            if u._username == username:
                return False
        return True

    # Check for if email is unique
    def email_is_unique(self, email: str) -> bool:
        for u in self._users:
            if u._email == email:
                return False
        return True

    # Search for User from Username
    def get_user_by_username(self, username: str) -> User:
        for u in self._users:
            if u._username == username:
                return u
        return None

    # Search for User from Email
    def get_user_by_email(self, email: str) -> User:
        for u in self._users:
            if u._email == email:
                return u
        return None
