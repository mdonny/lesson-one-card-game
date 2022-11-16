from tokenize import Special
from enums.CardProperty import CardProperty
from models.SpecialCard import SpecialCard


class PlusFour(SpecialCard):

    def __init__(self):
        super().__init__(CardProperty.PLUS_FOUR)

    def __str__(self):
        return "(t: %s, p: %s )" % (self.type, self.type_property)
