import random
from card import Card, Color, Deck

class Pyramid:
    class Cell:
        def __init__(self, card, lc=-1, rc=1):
            self.card = card
            self.lc = lc
            self.rc = rc
        
        def __str__(self):
            return self.card.to_string()

        def to_string(self):
            return self.card.to_string()


    def __init__(self, size):
        self.cells = []
        self.size = size
        card = Card()
        offset = 0
        
        for i in range(size):
            shift = offset

            for j in range(i, i*2):
                if i==size:
                    self.cells.append(Pyramid.Cell(card))
                else:
                    self.cells.append(Pyramid.Cell(card, j+shift, j+shift+1))
                offset += 1


class Board:
    def __init__(self, size):
        self.pyramid = Pyramid(size)

    def display(self):
        print('\n\n')
        cells = self.pyramid.cells
        rows = self.pyramid.size
        offset = 0

        for i in range(rows):
            for _ in range(rows-i):
                print('    ', end='')
            
            for _ in range(i):
                if cells[offset].card.color == Color.UNDEFINED:
                    if offset < 10:
                        print('[  ', offset, ' ] ', end='')
                    else:
                        print('[ ', offset, ' ] ', end='')             
                else:
                    if offset < 10:
                        print('[  ' + cells[offset].to_string() + ' ] ', end='')
                    else:
                        print('[ ' + cells[offset].to_string() + ' ] ', end='')
                offset +=1
            print('   ')


class Env:
    def __init__(self, conf):
        self.players = conf['players']
        self.players.append("local")
        self.floor = conf['floor']
        self.nb_card = conf['nb_card']
        self.nb_round = conf['nb_round']

        random.shuffle(self.players) 

    def reset(self):
        self.board = Board(self.floor)
        self.deck = Deck()
        self.deck.deal(len(self.players), self.nb_card)
        
        # set player is playing true
