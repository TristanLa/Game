from django import forms

class TourForm(forms.Form):
    TOUR_1 = 1
    TOUR_2 = 2
    TOUR_3 = 3
    EMPTY = ""

    TOUR_CHOICES = (
        (EMPTY, ""),
        (TOUR_1, 1),
        (TOUR_2, 2),
        (TOUR_3, 3),
    )

    tour_selected = forms.ChoiceField(label="Sélectionner le tour à afficher aux joueurs     ", choices=TOUR_CHOICES, initial=EMPTY)

class PlayerForm(forms.Form):
    player1_name = forms.CharField(label='Nom joueur 1', max_length=50)
    player2_name = forms.CharField(label='Nom joueur 2', max_length=50)
    player3_name = forms.CharField(label='Nom joueur 3', max_length=50)
    player4_name = forms.CharField(label='Nom joueur 4', max_length=50)