class Post:
    def __init__(self, id: int, user_id: int, date: int):
        self._id = id
        self._user_id = user_id
        self.content = None
        self.date = date
        self.views = 0
        self.likes = 0