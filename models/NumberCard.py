from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class NumberCard(ColoredCard):
    type_property = CardProperty.NUMBER

    def __init__(self, number, color):
        self.number = number
        super().__init__(color, self.type_property)

    def __str__(self):
        return "(t: %s, p: %s, c : %s, n: %d )" % (self.type, self.type_property, self.color, self.number)


