from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from perudo import forms, dice
from perudo.dice import Partie

# Create your views here.
def lost(request):
    return render(request, "perudo/lose.html", {})

def win(request):
    return render(request, "perudo/win.html", {})

def newgame(request):
    if request.method == 'POST':
        playersform = forms.PlayersForm(request.POST)

        if playersform.is_valid():
            dice.player_number = int(playersform.cleaned_data["players"])
            dice.init_dice_number = 5 * dice.player_number
            return HttpResponseRedirect(reverse("game", args=(dice.init_dice_number,)))
    else:
        playersform = forms.PlayersForm()

    context = {
        "playersform": playersform,
    }
    return render(request, "perudo/setup.html", context)


def game(request, dice_number):
    if dice_number == dice.init_dice_number:
        dice.perudo = dice.Partie(dice.player_number)

    player_dices = len(dice.perudo.player_dices)

    if request.method == 'POST' and 'win_btn' in request.POST:
        winform = forms.WinForm(request.POST)
        if winform.is_valid():
            dice.perudo.other_dices.pop()
            if len(dice.perudo.other_dices) == 0:
                return HttpResponseRedirect(reverse("won"))
            else:
                return HttpResponseRedirect(reverse("game", args=((len(dice.perudo.other_dices) + len(dice.perudo.player_dices)),)))
    elif request.method == 'POST' and 'lose_btn' in request.POST:
        loseform = forms.LoseForm(request.POST)
        if loseform.is_valid():
            dice.perudo.player_dices.pop()
            if len(dice.perudo.player_dices) == 0:
                return HttpResponseRedirect(reverse("lost"))
            else:
                return HttpResponseRedirect(reverse("game", args=((len(dice.perudo.other_dices) + len(dice.perudo.player_dices)),)))
    else:
        winform = forms.WinForm()
        loseform = forms.LoseForm()
        diceform = forms.DiceForm()

    context = {
        "player_dices": player_dices,
        "range": range(player_dices),
        "dice_number": dice_number,
        "player_number": dice.player_number,
        "winform": winform,
        "loseform": loseform,
        "diceform": diceform,
    }
    return render(request, "perudo/game.html", context)




