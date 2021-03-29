# Abstract Database Model
from abc import ABC, abstractmethod
from typing import List
from common.models.user import User
from common.models.post import Post
from common.models.comment import Comment


class AbstractDatabase(ABC):
    @abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def username_is_unique(self, username: str) -> bool:
        pass

    @abstractmethod
    def email_is_unique(self, username: str) -> bool:
        pass

    @abstractmethod
    def authenticate(self, user: User) -> User:
        pass
