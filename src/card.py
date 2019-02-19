from enum import Enum
import random

class Color(Enum):
    UNDEFINED = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    PURPLE = 5


class Card:
    def __init__(self, color=Color.UNDEFINED):
        self.color = color


    def __str__(self):
        return self.to_string()


    def to_string(self):
        switch_dict = {
            Color.UNDEFINED: 'X',
            Color.RED: 'R',
            Color.GREEN: 'G',
            Color.BLUE: 'B',
            Color.YELLOW: 'Y',
            Color.PURPLE: 'P'
        }

        return switch_dict[self.color]


class Deck:
    def __init__(self):
        self.cards = []

        for _ in range(7):
            self.cards.append(Card(Color.RED))
            self.cards.append(Card(Color.GREEN))
            self.cards.append(Card(Color.BLUE))
            self.cards.append(Card(Color.YELLOW))
            self.cards.append(Card(Color.PURPLE))
        
        self.cards.append(Card(Color.GREEN))


    def __str__(self):
        buffer = ""
        for card in self.cards:
            buffer += card.to_string() + " "
        return buffer


    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, nb_player, nb_card):
        hands = {}
        for i in range(nb_player):
            hands[i] = []

        for i in range(nb_card):
            for j in range(nb_player):
                hands[j].append(self.cards.pop())
        