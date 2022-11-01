from tokenize import Special
from enums.CardProperty import CardProperty
from models.SpecialCard import SpecialCard


class PlusFour(SpecialCard):
    type_property = CardProperty.PLUS_FOUR

    def __init__(self):
        super().__init__(self.type_property)

    def __str__(self):
        return "(t: %s, p: %s )" % (self.type, self.type_property)
