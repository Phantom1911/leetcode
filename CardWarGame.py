import random
from enum import Enum
from random import shuffle

from typing import List


class Suit(Enum):
    CLUB, DIAMOND, HEART, SPADE = range(4)


class Card:
    # @type
    def __init__(self: object, value: int, suit: Suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return str(self.value) + " " + self.suit.name


class Player:
    # @type
    def __init__(self: object, name: str, curr_cards: List[Card]):
        self.name = name
        self.curr_cards = curr_cards  # list of Card objects

    def draw_card(self):
        curr_num_of_cards = len(self.curr_cards)
        idx_of_drawn_card = random.randint(0, curr_num_of_cards - 1)
        drawn_card = self.curr_cards[idx_of_drawn_card]
        del self.curr_cards[idx_of_drawn_card]

        return drawn_card

    def add_to_curr_cards(self, to_add: List[Card]):
        if isinstance(to_add, List):
            self.curr_cards = self.curr_cards + to_add
        else:
            self.curr_cards.append(to_add)

    def print_curr_cards(self):
        for c in self.curr_cards:
            print(c.__repr__())


class Game:
    # @type
    def __init__(self: object, players: List[Player], cards: List[Card]):
        assert len(cards) % len(players) == 0, "The cards need to be equally divisible among players!"

        self.players = players  # list of Player objects
        self.cards = cards  # list of Card objects

    def distribute_cards(self):
        shuffle(self.cards)
        player_counter = 0
        for c in self.cards:
            self.players[player_counter % len(self.players)].add_to_curr_cards(c)
            player_counter += 1

    def start_game(self):
        print("the game is starting ..")
        print("distributing the cards ..")
        self.distribute_cards()
        print("after distribution ..")
        for player in self.players:
            print("---------- " + player.name + " CARDS  -----------------")
            player.print_curr_cards()
        print("num of cards " + str(len(self.players[0].curr_cards)))

        turn = 0
        curr_drawn_cards = []
        while True:
            drawn_card_one = self.players[turn].draw_card()
            drawn_card_two = self.players[~ turn].draw_card()
            curr_drawn_cards.append(drawn_card_one)
            curr_drawn_cards.append(drawn_card_two)
            if drawn_card_one.value > drawn_card_two.value:
                players[turn].add_to_curr_cards(curr_drawn_cards)
                curr_drawn_cards = []
            elif drawn_card_one.value < drawn_card_two.value:
                players[~turn].add_to_curr_cards(curr_drawn_cards)
                curr_drawn_cards = []

            if len(players[turn].curr_cards) == 0 or len(players[~turn].curr_cards) == 0:
                break
            turn = ~turn

        print("the game is over!")
        if len(self.players[0].curr_cards) == 0:
            print("the winner is " + str(self.players[1].name))
            print(self.players[1].print_curr_cards())
        else:
            print("the winner is " + str(self.players[0].name))
            print(self.players[0].print_curr_cards())

if __name__ == "__main__":
    p1 = Player("A", [])
    p2 = Player("B", [])
    players = [p1, p2]
    cards = []
    for s in Suit:
        for i in range(2, 15):
            c = Card(i, s)
            cards.append(c)

    game = Game(players, cards)
    game.start_game()
