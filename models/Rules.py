import random

from enums.Colors import Colors
from models.ColoredCard import ColoredCard
from models.SpecialCard import SpecialCard
from models.NumberCard import NumberCard
from enums.CardProperty import CardProperty
from models.BotPlayer import BotPlayer


class Rules:

    # Metodo che valida se la carta giocata è corretta in base alle regole del gioco
    @staticmethod
    def validate_card(player_card, table_card, table_current_color):
        if isinstance(player_card, SpecialCard) or isinstance(table_card, SpecialCard):
            if (
                    table_card.type_property == CardProperty.CHANGE_COLOUR or table_card.type_property == CardProperty.PLUS_FOUR) \
                    and isinstance(player_card, ColoredCard):
                return player_card.color == table_current_color
            return True

        if isinstance(player_card, ColoredCard) and isinstance(table_card, ColoredCard):
            if isinstance(player_card, NumberCard) and isinstance(table_card, NumberCard):
                return player_card.number == table_card.number or player_card.color == table_card.color
            if player_card.color == table_card.color:
                return True
        return False

    # Metodo che attiva le regole per le carte +2, +4 e cambia colore
    # assegnando 2/4 carte al giocatore avversario o cmbiando il colore del tavolo
    @staticmethod
    def activate_card_rules(card, player, next_player, table):
        if card.type_property == CardProperty.PLUS_FOUR:
            print("Card is +4 then add 4 cards to player " + next_player.name)
            for x in range(4):
                next_player.add_card(table.draw())
            Rules.change_color(player, table)

        if card.type_property == CardProperty.PLUS_TWO:
            print("Card is +2 then add 2 cards to player " + next_player.name)
            for x in range(2):
                next_player.add_card(table.draw())

        if card.type_property == CardProperty.CHANGE_COLOUR:
            Rules.change_color(player, table)


    # Metodo che cambia colore al tavolo
    @staticmethod
    def change_color(player, table):
        if isinstance(player, BotPlayer):
            color = player.select_change_color()
            print("Bot player color selected: " + str(color))
            table.current_color = color
        else:
            table.change_table_color()

    @staticmethod
    def select_random_color(table):
        color_list = [Colors.BLUE, Colors.GREEN, Colors.RED, Colors.YELLOW]
        color = random.randint(0, 4)
        print("Selected color is: " + str(color))
        table.current_color = color_list[color]



