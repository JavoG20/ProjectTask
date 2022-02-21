from card_deck import CardDeck

def main():
    start_game_dialogue()
    while True:
        play_game()
        print("\nQuieres jugar otra vez?: (y/n)")
        if input() != "y":
            print("\n\nGracias por jugar!")
            break

def start_game_dialogue():
    print("""Bienvenido a BlackJack en Python!
Empezemos con las reglas basicas:
    1. Usaremos una baraja que se mezcla cada vez que termina un juego.
    2. El As puede costar 1 o 11, depende de ti.
    3. Si te pasas de 21, pierdes y el dealer gana.
    4. Diviertete!
Cual es tu nombre?: """)
    name = input()
    print("\nOkay " + name + ", comenzemos el juego!")

def play_game():
    playing_deck = CardDeck()

    dealers_cards = {}
    dealer_hold = False
    dealer_score = 0

    players_cards = {}
    player_hold = False
    player_score = 0

    print("\n\nEl Dealer sacara dos cartas primero.")
    for i in range(2):
        try:
            dealer_score, dealers_cards, playing_deck = dealer_draw(dealer_score, dealers_cards, playing_deck)
        except TypeError:
            return

    print("\n\nTe toca sacar dos cartas.")
    for i in range(2):
        try:
            player_score, players_cards, playing_deck = player_draw(player_score, players_cards, playing_deck)
        except TypeError:
            return

    while not player_hold:
        print("Paras aqui?: (y/n)")
        if input() == "y":
            player_hold = True
            if(player_score < dealer_score):
                print("\nGana el Dealer!")
                return
        else:
            try:
                player_score, players_cards, playing_deck = player_draw(player_score, players_cards, playing_deck)
            except TypeError:
                return

    while not dealer_hold:
        if dealer_score >= 17:
            print("\nEl Dealer se queda!")
            dealer_hold = True
        else:
            try:
                dealer_score, dealers_cards, playing_deck = dealer_draw(dealer_score, dealers_cards, playing_deck)
            except TypeError:
                return

    if player_score > dealer_score:
        print("\nGanaste!")
    elif dealer_score > player_score:
        print("\nGana el Dealer")
    else:
        print("\nEs un Empate!")

def dealer_logic(current_score):
    if current_score <= 10:
        return True
    return False

def player_draw(player_score, players_cards, playing_deck):
    card_tuple = playing_deck.draw_card()
    if card_tuple[0][0] == "A":
        print("Sacaste un As. Quieres que valga 1 o 11?: (1/11)")
        players_cards[card_tuple[0]] = int(input())
        player_score += players_cards[card_tuple[0]]
        print("\n\nTu Puntaje: " + str(player_score) + "\nTus Cartas: ")
        print_cards(players_cards)
    else:
        players_cards[card_tuple[0]] = card_tuple[1]
        player_score += card_tuple[1]
        print("\n\nTu Puntaje: " + str(player_score) + "\nTus Cartas: ")
        print_cards(players_cards)
    if player_score == 21:
        print("\nTienes 21. Ganaste!")
        return
    if player_score > 21:
        print("\nTe pasaste! Gana el Dealer")
        return
    return (player_score, players_cards, playing_deck)

def dealer_draw(dealer_score, dealers_cards, playing_deck):
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
    print("\n\nPuntaje del Dealer: " + str(dealer_score) + "\nCartas Dealer: ")
    print_cards(dealers_cards)
    if dealer_score == 21:
        print("\nEl dealer tiene 21. Perdiste!")
        return
    elif dealer_score > 21:
        print("\nEl Dealer se paso. Ganas!")
        return
    return(dealer_score, dealers_cards, playing_deck)

def print_cards(cards):
    for card in cards:
        print(card)

main()
