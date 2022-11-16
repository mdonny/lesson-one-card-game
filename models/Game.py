from models.Player import Player
from models.SpecialCard import SpecialCard
from models.Table import Table
from models.ChangeLap import ChangeLap
from models.ProhibitionCard import ProhibitionCard
import random


class Game:
    first_names = ('John', 'Andy', 'Joe')
    last_names = ('Johnson', 'Smith', 'Williams')

    def __init__(self, players_number, bot_numbers):
        self.players = []
        self.player_numbers = players_number
        self.bot_numbers = bot_numbers
        self.table = Table()

    def generate_player(self):
        pass

    def initialize_players_cards(self):
        pass

    def add_player(self, player):
        pass

    def player_draw_card(self, player):
        pass

    def play_game(self):
        finish = False
        winner = ""
        while not self.table.check_deck_is_empty() and not finish:
            pass
        print("The player winner is: " + winner)

    def play_turn(self, player, next_player):
        pass

    def choose_play(self):
        print("Select your action: 0-n - Play Card, d - Draw card")
        action = input()
        print("Your selected action is: " + action)
        if (action.isnumeric() and int(action) < 0) or (not action.isnumeric() and action != "d"):
            print("Bad selection, retry")
            self.choose_play()
        return action
