from typing import List

from splitwise.User import User


class service:
    def __init__(self, players: List[User]):
        self.players = players

    def start_game(self):
        print('now we are playing game')
        print(self.players[0].name)
