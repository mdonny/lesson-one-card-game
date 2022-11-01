from mimetypes import init
from models.ProhibitionCard import ProhibitionCard
from models.PlusTwo import PlusTwo
from models.ChangeLap import ChangeLap
from models.PlusFour import PlusFour
from enums.Colors import Colors
from models.ChangeColour import ChangeColour
from models.NumberCard import NumberCard
from models.ColoredCard import ColoredCard
import random


class Table:

    def __init__(self):
        self.deck = []
        self.played_cards = []
        self.current_color = Colors.BLUE

    def generate_cards(self):
        for x in range(0, 4):
            current_color = Colors(x)
            for y in range(0, 10):
                if y > 0:
                    self.deck.append(NumberCard(y, current_color))
                self.deck.append(NumberCard(y, current_color))
            self.deck.append(ProhibitionCard(current_color))
            self.deck.append(ProhibitionCard(current_color))
            self.deck.append(PlusTwo(current_color))
            self.deck.append(PlusTwo(current_color))
            self.deck.append(ChangeLap(current_color))
            self.deck.append(ChangeLap(current_color))
            self.deck.append(PlusFour())
            self.deck.append(ChangeColour())

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def string_deck(self):
        return '\n'.join(str(x) for x in self.deck)

    def check_deck_is_empty(self):
        return len(self.deck) == 0

    def play_card(self, card):
        self.played_cards.append(card)
        if isinstance(card, ColoredCard):
            self.current_color = card.color
        else:
            self.current_color = None

    def show_last_played_card(self):
        return self.played_cards[len(self.played_cards) - 1]

    def change_table_color(self):
        print("Select a color: 1 - Red, 2 - Yellow, 3 - Green, 4 - Blue")
        color = int(input())
        if color == 1:
            print("Selected RED color!")
            self.current_color = Colors.RED
        elif color == 2:
            print("Selected YELLOW color!")
            self.current_color = Colors.YELLOW
        elif color == 3:
            print("Selected GREEN color!")
            self.current_color = Colors.GREEN
        elif color == 4:
            print("Selected BLUE color!")
            self.current_color = Colors.BLUE
        else:
            print("Selection wrong, retry!")
            self.change_table_color()
