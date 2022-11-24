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
        card = self.table.draw()
        self.table.play_card(card)
        print("Game launched")

    # Metodo che genera i players
    def generate_player(self):
        how_many_human = self.player_numbers - self.bot_numbers
        for x in range(how_many_human):
            print("Insert payer name")
            player_name = input()
            print("Player name is: %s" % player_name)
            current_player = Player(player_name)
            self.add_player(current_player)
        self.initialize_players_cards()

    #    Metodo che inizializza le carte dei giocatori
    def initialize_players_cards(self):
        for player in self.players:
            for x in range(7):
                card = self.table.draw()
                player.add_card(card)

    #    Metodo che aggiunge un giocatore
    def add_player(self, player):
        self.players.append(player)

    #    Metodo che gioca una carta
    def player_draw_card(self, player):
        card = self.table.draw()
        player.add_card(card)

    # Metodo che implementa il motore del gioco
    def play_game(self):
        finish = False
        winner = ""
        while not self.table.check_deck_is_empty() and not finish:
            pass
        print("The player winner is: " + winner)

    # Metodo che implementa il turno di gioco
    def play_turn(self, player, next_player):
        pass

    # Metodo che sceglie la carta d agiocare
    def choose_play(self):
        print("Select your action: 0-n - Play Card, d - Draw card")
        valid_action = False
        while not valid_action:
            action = input()
            print("Your selected action is: " + action)
            if (action.isnumeric() and int(action) > 0) or (not action.isnumeric() and action == "d"):
                valid_action = True
            else:
                print("Bad selection, retry")
        return action

