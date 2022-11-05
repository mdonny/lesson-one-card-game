# Introduzione

Questa è la prima parte di programma python di esempio che implementa il gioco di carte Uno https://it.wikipedia.org/wiki/UNO_(gioco_di_carte)

La lista di tutte le carte del gioco le possiamo trovare in questa immagine (fornita da wikipedia): 

![UNO_cards_deck svg](https://user-images.githubusercontent.com/40794836/199604045-9f9ba18b-ca7d-41e8-aaae-de979a169a0b.png)

## Suddivisione progetto

Il progetto è suddiviso su 2 cartelle principali, *enums* e *models*.

La cartella *enums* contiene gli enumeratori che saranno usati poi dalle varie classi.
La cartella *models* contiene le classi che saranno poi utili al programma.

## Obiettivo lezione 1

In questa prima lezione si andranno ad implementare le classi per le varie tipologie di carte, le carte in questione sono:

- Carta numero 
- Carta Cambio giro
- Carta Divieto (Salta)
- Carta Pesca 2 carte
- Carta Cambia colore
- Carta Pesca 4 carte

Una volta create le carte andremo ad inizializzare il mazzo di 108 carte nel main del progetto. 

## Obiettivo extra

Creare una classe Tavolo che abbia una proprietà mazzo e che questo sia inizializzato nel costruttore con tutte le carte del gioco.

#### Esempio dell'implementazione della carta numero

```
from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class NumberCard(ColoredCard):
    def __init__(self, number, color):
        self.number = number
        super().__init__(color, CardProperty.NUMBER)

    def __str__(self):
        return "(t: %s, p: %s, c : %s, n: %d )" % (self.type, self.type_property, self.color, self.number)
```
