import random
#importamos random para poder usar random.randit(1, 6) para obtener un "dado" del 1 al 6

#La primera class es Player, tiene su name, sus monedas recolectadas, su vida, su posicion, y sus items.
class Player:

    def __init__(self, name):
        self.name = name
        self.coins = 15
        self.health = 15
        self.position = {}
        self.dice = 0
        self.items = []

    def __repr__(self):
        return "{name} tiene {coins} monedas, y le quedan estos objetos: {items}, y se encuentra en el tile numero {tile}.".format(name = self.name, coins = self.coins, items  self.bag, tile = self.position)

    def roll_dice(self):
        min_dice = 1
        max_dice = 6
        dices = random.randit(min_dice, max_dice)
        self.dice += dices
        return dices


    def play(self):
        while True:
            user_prompt = input("> ")
            if user_prompt.lower() = "quit":
                return False
            else:
                print("Girando el dado....\n Tu numero es: {}".format(roll_dice))

    def advance_position(self):
        position = self.position
        for key, value in position:
            key = self.dice
            lose_coin = self.coins - 2
            add_coin = self.coins + 2
            if key % 2 == 0:
                self.position[key] = lose_coin
                print("Pierdes dos monedas pendejo.")
            elif key == 1 or 3 or 5:
                self.position[key] = add_coin
                print("Ojo! Ganaste 2 monedas pedazo de imbecil!")
            else:
                self.position[key]
                print("Avanzale wey.")
        return self.position




#Estos son para obtener el nombre del Jugador. player_one_name para ver cual es su nombre.
#Despues player_one lo asignamos a la class de Player, con player_one_name como su name.
player_one_name = input("Bienvenido al Teton Party, cual es tu perro nombre? ")
player_one = Player(player_one_name)
