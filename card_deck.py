import random

class CardDeck():
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    royalty = ["Jack", "Queen", "King"]

    def __init__(self):
        """
        Creates a card deck of 52 cards.
        """
        self.deck = {}
        for suit in CardDeck.suits:
            self.deck["Ace of " + suit] = 1
            for i in range(2,11):
                self.deck[str(i) + " of " + suit] = i
            for royal_member in CardDeck.royalty:
                self.deck[royal_member + " of " + suit] = 10

    def draw_card(self):
        """
        Picks a random card out of the deck, removes it from the dictionary, and returns it and its value.
        :returns a tuple with the card name and value:
        """
        card_of_choice = random.choice(list(self.deck.keys()))
        return (card_of_choice, self.deck.pop(card_of_choice))
