from enums.Colors import Colors
from models.ColoredCard import ColoredCard
from models.NumberCard import NumberCard
from models.Player import Player
from models.SpecialCard import SpecialCard


class BotPlayer(Player):

    def select_what_play(self, field_card, table_color):
        print("Field card is: " + str(field_card))
        print("Your hand is: \n" + self.show_hand())
        count = 0
        for card in self.hand:
            current_card = self.card_logic(card, field_card, table_color)
            if current_card:
                print("Card to play is: " + str(card))
                del self.hand[count]
                return card
            count += 1
        return None

    def card_logic(self, my_card, field_card, table_color):
        if isinstance(field_card, NumberCard):
            if isinstance(my_card, NumberCard):
                if my_card.color == field_card.color:
                    return True
                elif my_card.number == field_card.number:
                    return True
            if isinstance(my_card, SpecialCard):
                return True
        if isinstance(field_card, ColoredCard):
            if isinstance(my_card, ColoredCard) and my_card.color == field_card.color:
                return True
            if isinstance(my_card, SpecialCard):
                return True
        if isinstance(field_card, SpecialCard):
            if isinstance(my_card, ColoredCard) and my_card.color == table_color:
                return True
            if isinstance(my_card, SpecialCard):
                return True
        return False

    def select_change_color(self):
        red = 0
        yellow = 0
        blue = 0
        green = 0
        for card in self.hand:
            if isinstance(card, ColoredCard):
                if card.color == Colors.RED:
                    red += 1
                if card.color == Colors.GREEN:
                    green += 1
                if card.color == Colors.BLUE:
                    blue += 1
                if card.color == Colors.YELLOW:
                    yellow += 1
        if red >= yellow and red >= blue and red >= green:
            return Colors.RED
        if yellow >= red and yellow >= blue and yellow >= green:
            return Colors.YELLOW
        if blue >= red and blue >= yellow and blue >= green:
            return Colors.BLUE
        if green >= red and green >= yellow and green >= blue:
            return Colors.GREEN
