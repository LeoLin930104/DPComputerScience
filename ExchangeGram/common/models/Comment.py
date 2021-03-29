class Comment:
    def __init__(self, post_id: int, user_id: int, date: int):
        self._id = 0
        self._post_id = post_id
        self._user_id = user_id
        self.content = None
        self.date = date
        self.likes = 0