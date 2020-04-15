from django.shortcuts import render, reverse
from toc import cards, forms
from django.http import HttpResponseRedirect



# Create your views here.
def dealer(request, tour=1):
    if cards.d:
        d = cards.d
    else:
        d = cards.d_new
    if request.method == 'POST':
        tourform = forms.TourForm(request.POST)
        if tourform.is_valid():
            tour = tourform.cleaned_data["tour_selected"]
            return HttpResponseRedirect(reverse("toc-tour", args=(tour,)))

    else:
        tourform = forms.TourForm()

    cards.lap = tour

    context = {
        "tourform": tourform,
        "tour": tour,
        'd': d,
        'card_img': cards.card_img,
    }
    return render(request, "toc/dealer.html", context)

def player(request, name):
    if cards.d:
        d = cards.d
    else:
        d = cards.d_new

    tour = cards.lap

    context = {
        "name": name,
        "tour": tour,
        'd': d,
        'card_img': cards.card_img,
    }
    return render(request, "toc/player.html", context)

def new_deal(request):
    if cards.d:
        cards.d.clear()
        cards.d_new = cards.Deal()
    else:
        cards.d_new.clear()
        cards.d = cards.Deal()

    if request.method == 'POST':
        playerform = forms.PlayerForm(request.POST)

        if playerform.is_valid():
            cards.p1 = playerform.cleaned_data["player1_name"]
            cards.p2 = playerform.cleaned_data["player2_name"]
            cards.p3 = playerform.cleaned_data["player3_name"]
            cards.p4 = playerform.cleaned_data["player4_name"]
    else:
        playerform = forms.PlayerForm()

    context = {
        "playerform": playerform,
    }

    return render(request, "toc/newdeal.html", context)
