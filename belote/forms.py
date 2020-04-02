from django import forms

class PlayerForm(forms.Form):
    player1_name = forms.CharField(label='Nom joueur 1', max_length=50)
    player2_name = forms.CharField(label='Nom joueur 2', max_length=50)
    player3_name = forms.CharField(label='Nom joueur 3', max_length=50)
    player4_name = forms.CharField(label='Nom joueur 4', max_length=50)