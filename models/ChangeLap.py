from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class ChangeLap(ColoredCard):
    type_property = CardProperty.CHANGE_LAP

    def __init__(self, color):
        super().__init__(color, self.type_property)

    def __str__(self):
        return "(t: %s, p: %s, c: %s )" % (self.type, self.type_property, self.color)


