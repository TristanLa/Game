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


p1 = "Jérôme"
p2 = "Marie-Françoise"
p3 = "Baptiste"
p4 = "Tristan"

def Deal():
    deck = Deck()
    Player1 = []
    Player2 = []
    Player3 = []
    Player4 = []
    d = {
        p1: Player1,
        p2: Player2,
        p3: Player3,
        p4: Player4,
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
    return d

card_img = {
    "As de Trèfle": "img/01-trefle.png",
    "Deux de Trèfle": "img/02-trefle.png",
    "Trois de Trèfle": "img/03-trefle.png",
    "Quatre de Trèfle": "img/04-trefl.png",
    "Cinq de Trèfle": "img/05-trefle.png",
    "Six de Trèfle": "img/06-trefle.png",
    "Sept de Trèfle": "img/07-trefle.png",
    "Huit de Trèfle": "img/08-trefle.png",
    "Neuf de Trèfle": "img/09-trefle.png",
    "Dix de Trèfle": "img/10-trefle.png",
    "Valet de Trèfle": "img/Valet-trefle.png",
    "Dame de Trèfle": "img/Dame-trefle.png",
    "Roi de Trèfle": "img/Roi-trefle.png",
    "As de Coeur": "img/01-coeur.png",
    "Deux de Coeur": "img/02-coeur.png",
    "Trois de Coeur": "img/03-coeur.png",
    "Quatre de Coeur": "img/04-coeur.png",
    "Cinq de Coeur": "img/05-coeur.png",
    "Six de Coeur": "img/06-coeur.png",
    "Sept de Coeur": "img/07-coeur.png",
    "Huit de Coeur": "img/08-coeur.png",
    "Neuf de Coeur": "img/09-coeur.png",
    "Dix de Coeur": "img/10-coeur.png",
    "Valet de Coeur": "img/Valet-coeur.png",
    "Dame de Coeur": "img/Dame-coeur.png",
    "Roi de Coeur": "img/Roi-coeur.png",
    "As de Pique": "img/01-pique.png",
    "Deux de Pique": "img/02-pique.png",
    "Trois de Pique": "img/03-pique.png",
    "Quatre de Pique": "img/04-pique.png",
    "Cinq de Pique": "img/05-pique.png",
    "Six de Pique": "img/06-pique.png",
    "Sept de Pique": "img/07-pique.png",
    "Huit de Pique": "img/08-pique.png",
    "Neuf de Pique": "img/09-pique.png",
    "Dix de Pique": "img/10-pique.png",
    "Valet de Pique": "img/Valet-pique.png",
    "Dame de Pique": "img/Dame-pique.png",
    "Roi de Pique": "img/Roi-pique.png",
    "As de Carreau": "img/01-carreau.png",
    "Deux de Carreau": "img/02-carreau.png",
    "Trois de Carreau": "img/03-carreau.png",
    "Quatre de Carreau": "img/04-carreau.png",
    "Cinq de Carreau": "img/05-carreau.png",
    "Six de Carreau": "img/06-carreau.png",
    "Sept de Carreau": "img/07-carreau.png",
    "Huit de Carreau": "img/08-carreau.png",
    "Neuf de Carreau": "img/09-carreau.png",
    "Dix de Carreau": "img/10-carreau.png",
    "Valet de Carreau": "img/Valet-carreau.png",
    "Dame de Carreau": "img/Dame-carreau.png",
    "Roi de Carreau": "img/Roi-carreau.png",
    }

d = Deal()
d_new = {}

