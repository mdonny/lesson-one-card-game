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
        pass

    def shuffle(self):
        pass

    def draw(self):
        pass

    def string_deck(self):
        pass

    def check_deck_is_empty(self):
        return len(self.deck) == 0

    def play_card(self, card):
        pass

    def show_last_played_card(self):
        pass

    def change_table_color(self):
        pass
