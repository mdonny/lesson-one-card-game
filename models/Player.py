class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_card_number(self):
        return len(self.hand)

    def show_hand(self):
        count = 0
        cards = ""
        for x in self.hand:
            cards += str(count) + " - " + str(x) + "\n"
            count += 1
        return cards

    def play_card(self, index):
        if index > len(self.hand):
            print("Error select card, retry")
            self.play_card()
        return self.hand.pop(index)
