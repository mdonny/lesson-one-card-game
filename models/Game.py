from models.Player import Player
from models.SpecialCard import SpecialCard
from models.Table import Table
from models.Rules import Rules
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
        self.table.generate_cards()
        self.table.shuffle()
        card = self.table.draw()
        self.table.play_card(card)
        self.table.play_card(card)
        if isinstance(card, SpecialCard):
            Rules.select_random_color(self.table)
        self.generate_player()
        print("Deck size after dispatch cards: %d" % (len(self.table.deck)))
        for player in self.players:
            print("Player %s have %d cards" % (player.name, player.get_hand_card_number()))
        self.play_game()

    # Metodo che genera i players
    def generate_player(self):
        for x in range(self.player_numbers):
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
        count = 0
        while not self.table.check_deck_is_empty() and not finish:
            if len(self.table.played_cards) > 0:
                if isinstance(self.table.show_last_played_card(), ChangeLap):
                    self.players.reverse()
                if isinstance(self.table.show_last_played_card(), ProhibitionCard):
                    count += 1
            if count < self.player_numbers:
                player = self.players[count]
                if count == self.player_numbers - 1:
                    next_player = self.players[0]
                else:
                    next_player = self.players[count + 1]
                print("Player %s is tour turn" % player.name)
                self.play_turn(player, next_player)
                if player.get_hand_card_number() <= 0:
                    finish = True
                    winner = player.name
                count += 1
            else:
                count = 0
        print("The player winner is: " + winner)

    # Metodo che implementa il turno di gioco
    def play_turn(self, player, next_player):
        print("Last played card is: " + str(
            self.table.show_last_played_card()) + " and current color: " + str(self.table.current_color or ''))
        print("Your hand is: \n" + player.show_hand())
        action = self.choose_play()
        if action.isnumeric():
            card = player.play_card(int(action))
            print("Player play card: " + str(card))
            if Rules.validate_card(card, self.table.show_last_played_card(), self.table.current_color):
                print("Card is valid!")
                self.table.play_card(card)
                Rules.activate_card_rules(card, player, next_player, self.table)
            else:
                print("Card played is wrong, retry!")
                player.add_card(card)
                self.play_turn(player, next_player)
        else:
            print("Player draw a card!")
            player.add_card(self.table.draw())

    # Metodo che sceglie la carta d agiocare
    def choose_play(self):
        print("Select your action: 0-n - Play Card, d - Draw card")
        valid_action = False
        while not valid_action:
            action = input()
            print("Your selected action is: " + action)
            if (action.isnumeric() and int(action) >= 0) or (not action.isnumeric() and action == "d"):
                valid_action = True
            else:
                print("Bad selection, retry")
        return action
