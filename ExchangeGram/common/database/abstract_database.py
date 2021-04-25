# Abstract Database Model
from abc import ABC, abstractmethod
from typing import List
from common.models.User import User
from common.models.Post import Post
from common.models.Comment import Comment


class AbstractDatabase(ABC):
    @abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def create_post(self, post: Post) -> Post:
        pass

    @abstractmethod
    def delete_post(self, post: Post) -> bool:
        pass

    @abstractmethod
    def update_post(self, post: Post) -> Post:
        pass

    @abstractmethod
    def create_comment(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def delete_comment(self, comment: Comment) -> bool:
        pass

    @abstractmethod
    def update_comment(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def username_is_unique(self, username: str) -> bool:
        pass

    @abstractmethod
    def email_is_unique(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_username(self, usernmae: str) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass
