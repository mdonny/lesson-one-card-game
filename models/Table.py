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

# Metodo che genera il deck da gioco
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

    # Metodo che mescola il deck da gioco
    def shuffle(self):
        pass

    # Metodo che pesca una carta dal deck
    def draw(self):
        pass

    # Metodo che stampa la lista di carte del deck
    def string_deck(self):
        pass

    def check_deck_is_empty(self):
        return len(self.deck) == 0

    # Metodo che gioca una carta e la aggiunge alle carte in gioco
    def play_card(self, card):
        pass

    # Metodo che mostra l'ultima carta giocata
    def show_last_played_card(self):
        pass

    # Metodo che gestisce la carta cambia colore
    def change_table_color(self):
        pass
