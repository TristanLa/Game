import random

class Card:
    color_name = ["Coeur", "Carreau", "Trèfle", "Pique",]
    value_name = ["Sept", "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As"]

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return "{} de {}".format(Card.value_name[self.value], Card.color_name[self.color])

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0,len(Card.color_name)):
            for j in range(0,len(Card.value_name)):
                self.cards.append(Card(i,j))

    def __str__(self):
        for card in self.cards:
            print(str(card))


def Deal():
    deck = Deck()
    Player1 = []
    Player2 = []
    Player3 = []
    Player4 = []
    d = {
        'Player1': Player1,
        'Player2': Player2,
        'Player3': Player3,
        'Player4': Player4,
    }
    for i in range(0, 8):
        a = random.randint(0, len(deck.cards)-1)
        Player1.append(str(deck.cards[a]))
        deck.cards.pop(a)
    for i in range(0, 8):
        a = random.randint(0, len(deck.cards)-1)
        Player2.append(str(deck.cards[a]))
        deck.cards.pop(a)
    for i in range(0, 8):
        a = random.randint(0, len(deck.cards)-1)
        Player3.append(str(deck.cards[a]))
        deck.cards.pop(a)
    for i in range(0, 8):
        a = random.randint(0, len(deck.cards)-1)
        Player4.append(str(deck.cards[a]))
        deck.cards.pop(a)
    for i in d:
        print(i,"has the following cards:")
        for j in d[i]:
            print(j)

Deal()