class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    # Metodo che aggiunge una carta alla mano del giocatore
    def add_card(self, card):
        pass

    # Metodo che stampa il numero di carte nella mano del giocatore
    def get_hand_card_number(self):
        return len(self.hand)

    # Metodo che stampa la mano del giocatore
    def show_hand(self):
        pass

    # Metodo che permette al giocatore di giocare una carta dopo averla scelta
    def play_card(self, index):
        pass
