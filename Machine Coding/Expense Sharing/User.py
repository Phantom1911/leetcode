from collections import defaultdict
class User:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.user_owings = defaultdict(int)
