from enums.CardProperty import CardProperty
from models.SpecialCard import SpecialCard


class ChangeColour(SpecialCard):

    def __init__(self):
        super().__init__(CardProperty.CHANGE_COLOUR)

    def __str__(self):
        return "(t: %s, p: %s )" % (self.type, self.type_property)
