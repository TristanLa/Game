from django import forms
from perudo import views

class PlayersForm(forms.Form):
    Players_2 = 2
    Players_3 = 3
    Players_4 = 4
    Players_5 = 5
    Players_6 = 6
    EMPTY = ""

    CHOICES = (
        (Players_2, 2),
        (Players_3, 3),
        (Players_4, 4),
        (Players_5, 5),
        (Players_6, 6),
        (EMPTY, ""),
    )

    players = forms.ChoiceField(label="Quel est le nombre de joueurs pour cette partie? ", choices=CHOICES, initial=EMPTY)

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
class WinForm(forms.Form):
    pass

class LoseForm(forms.Form):
    pass
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
class DiceForm(forms.Form):
    Dice_1 = 1
    Dice_2 = 2
    Dice_3 = 3
    Dice_4 = 4
    Dice_5 = 5
    Dice_6 = 6
    EMPTY = ""

    CHOICES = (
        (Dice_1, 1),
        (Dice_2, 2),
        (Dice_3, 3),
        (Dice_4, 4),
        (Dice_5, 5),
        (Dice_6, 6),
        (EMPTY, ""),
    )

    dice_value = forms.ChoiceField(label="", choices=CHOICES, initial=EMPTY)

