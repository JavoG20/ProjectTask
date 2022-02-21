import random

class CardDeck():
    suits = ["Corazones", "Espadas", "Diamantes", "Treboles"]
    royalty = ["Joto", "Reyna", "Rey"]

    def __init__(self):
        self.deck = {}
        for suit in CardDeck.suits:
            self.deck["As de " + suit] = 1
            for i in range(2,11):
                self.deck[str(i) + " de " + suit] = i
            for royal_member in CardDeck.royalty:
                self.deck[royal_member + " de " + suit] = 10

    def draw_card(self):
        card_of_choice = random.choice(list(self.deck.keys()))
        return (card_of_choice, self.deck.pop(card_of_choice))
