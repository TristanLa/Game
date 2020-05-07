import random

class Dice:
    def __init__(self):
        self.value = 0

    def __str__(self):
        return "Dé de valeur {}".format(self.value)

class Player:
    def __init__(self):
        self.dice_number = 5
        self.dices = []
        for i in range(0, self.dice_number):
            self.dices.append(Dice())

    def __str__(self):
        return "Joueur {} avec {} dés".format(self.name, self.dices)

class Partie:
    def __init__(self, player_number):
        self.player_number = player_number
        self.player_dices = Player().dices
        self.other_dices = []
        for i in range(1, self.player_number):
            self.other_dices.extend(Player().dices)

        self.dice_number = len(self.player_dices) + len(self.other_dices)

    def __str__(self):
        return "La partie comporte {} joueurs avec au total {} dés".format(self.player_number, self.dice_number)

dice_img = {
    "Dé de valeur 0": "img/dice_0.png",
    "Dé de valeur 1": "img/dice_1.png",
    "Dé de valeur 2": "img/dice_2.png",
    "Dé de valeur 3": "img/dice_3.png",
    "Dé de valeur 4": "img/dice_4.png",
    "Dé de valeur 5": "img/dice_5.png",
    "Dé de valeur 6": "img/dice_6.png",
}

player_number = 0
init_dice_number = 0
perudo = Partie(1)
