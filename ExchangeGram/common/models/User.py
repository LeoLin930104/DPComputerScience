class User:
    def __init__(self, username: str, email: str, password_hash: str):
        self._id = 0
        self._username = username
        self._password_hash = password_hash
        self._email = email
        self.follows = []

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        self.username = username

    @property
    def email_address(self) -> str:
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        self.email_address = email_address

    def add_following(self, user_id: int) -> None:
        self.following.append(user_id)
