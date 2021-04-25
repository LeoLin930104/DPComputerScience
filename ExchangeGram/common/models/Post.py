class Post:
    def __init__(self, user_id: int, content: str, date: int):
        self._id = 0
        self._user_id = user_id
        self.content = content
        self.date = date
        self.views = 0
        self.likes = 0