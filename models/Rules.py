import random

from enums.Colors import Colors
from models.ColoredCard import ColoredCard
from models.SpecialCard import SpecialCard
from models.NumberCard import NumberCard
from enums.CardProperty import CardProperty


class Rules:

    # Metodo che valida se la carta giocata è corretta in base alle regole del gioco
    @staticmethod
    def validate_card(player_card, table_card, table_current_color):
        pass

    # Metodo che attiva le regole per le carte +2, +4 e cambia colore
    # assegnando 2/4 carte al giocatore avversario o cmbiando il colore del tavolo
    @staticmethod
    def activate_card_rules(card, player, next_player, table):
        pass


    # Metodo che cambia colore al tavolo
    @staticmethod
    def change_color(player, table):
        pass



