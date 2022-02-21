from card_deck import CardDeck

def main():
    start_game_dialogue()
    while True:
        play_game()
        print("\nDo you want to play again?: (y/n)")
        if input() != "y":
            print("\n\nThanks for playing!")
            break

def start_game_dialogue():
    print("""Welcome to BlackJack in Python!
Let's start with some rules of how our game will be played:
    1. We will use one deck of cards that is reshuffled after every deal.
    2. It is up to you whether an Ace is worth 1 point or 11 points.
    3. If you go over 21 points, you will bust and the dealer wins.
    4. Have fun!
To start playing, what is your name?: """)
    name = input()
    print("\nOkay " + name + ", let's start playing!")

def play_game():
    """
    Plays one full game of blackjack, with just the player and the dealer.
    """
    playing_deck = CardDeck()

    dealers_cards = {}
    dealer_hold = False
    dealer_score = 0

    players_cards = {}
    player_hold = False
    player_score = 0

    print("\n\nThe dealer will draw two cards first.")
    for i in range(2):
        #An error had to be excepted if the method for drawing returned None (which means an end result was reached)
        try:
            dealer_score, dealers_cards, playing_deck = dealer_draw(dealer_score, dealers_cards, playing_deck)
        except TypeError:
            return

    print("\n\nYou will draw two cards now.")
    for i in range(2):
        try:
            player_score, players_cards, playing_deck = player_draw(player_score, players_cards, playing_deck)
        except TypeError:
            return

    while not player_hold:
        print("Do you want to stand?: (y/n)")
        if input() == "y":
            player_hold = True
            if(player_score < dealer_score):
                print("\nDealer wins!")
                return
        else:
            try:
                player_score, players_cards, playing_deck = player_draw(player_score, players_cards, playing_deck)
            except TypeError:
                return

    while not dealer_hold:
        if dealer_score >= 17:
            print("\nThe dealer has held!")
            dealer_hold = True
        else:
            try:
                dealer_score, dealers_cards, playing_deck = dealer_draw(dealer_score, dealers_cards, playing_deck)
            except TypeError:
                return

    if player_score > dealer_score:
        print("\nYou win!")
    elif dealer_score > player_score:
        print("\nThe dealer wins!")
    else:
        print("\nIt's a tie!")

def dealer_logic(current_score):
    """
    Used if the dealer encounters an ace. If the dealer can take a score of 11 without busting, return True.
    If not, return False.
    """
    if current_score <= 10:
        return True
    return False

def player_draw(player_score, players_cards, playing_deck):
    """
    Draws a card for the player and passes in the three parameters of the same name in the parent method.
    :returns a tuple with the three updated parameters unless an end result was reached:
    """
    card_tuple = playing_deck.draw_card()
    if card_tuple[0][0] == "A":
        print("You've drawn an Ace. Would you like it to be worth 1 or 11 points?: (1/11)")
        players_cards[card_tuple[0]] = int(input())
        player_score += players_cards[card_tuple[0]]
        print("\n\nYour Score: " + str(player_score) + "\nYour Cards: ")
        print_cards(players_cards)
    else:
        players_cards[card_tuple[0]] = card_tuple[1]
        player_score += card_tuple[1]
        print("\n\nYour Score: " + str(player_score) + "\nYour Cards: ")
        print_cards(players_cards)
    if player_score == 21:
        print("\nYou have played 21. You win!")
        return
    if player_score > 21:
        print("\nYou have busted! Dealer wins!")
        return
    return (player_score, players_cards, playing_deck)

def dealer_draw(dealer_score, dealers_cards, playing_deck):
    """
    Draws a card for the dealer and passes in the three parameters of the same name in the parent method.
    :returns a tuple with the three updated parameters unless an end result was reached:
    """
    card_tuple = playing_deck.draw_card()
    if card_tuple[0][0] == "A":
        if dealer_logic(dealer_score):
            dealers_cards[card_tuple[0]] = 11
            dealer_score += 11
        else:
            dealers_cards[card_tuple[0]] = 1
            dealer_score += 1
    else:
        dealers_cards[card_tuple[0]] = card_tuple[1]
        dealer_score += card_tuple[1]
    print("\n\nDealer's Score: " + str(dealer_score) + "\nDealer's Cards: ")
    print_cards(dealers_cards)
    if dealer_score == 21:
        print("\nThe dealer has played 21. You lose!")
        return
    elif dealer_score > 21:
        print("\nThe dealer busted, you win!")
        return
    return(dealer_score, dealers_cards, playing_deck)

def print_cards(cards):
    """
    Prints out each individual card name in the cards dictionary.
    """
    for card in cards:
        print(card)

main()
