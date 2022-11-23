from enums.Colors import Colors
from models.ColoredCard import ColoredCard
from models.NumberCard import NumberCard
from models.Player import Player
from models.SpecialCard import SpecialCard


class BotPlayer(Player):

    # Metodo che fa scegliere al bot cosa giocare (Pesco o gioco una carta)?
    def select_what_play(self, field_card, table_color):
        pass

    # Metodo che una volta che decido di giocare una carta
    # Fa scegliere quale carta giocare
    def card_logic(self, my_card, field_card, table_color):
        pass

    # Metodo per far scegliere al bot il colore della carta cambia colore in base
    # alle carte che ho in mano
    def select_change_color(self):
        pass
