from django.shortcuts import render
from belote import cards

def dealer(request, name=""):
    if cards.d:
        d = cards.d
    else:
        d = cards.d_new

    context = {
        "name":name,
        'd': d,
        'card_img': cards.card_img,
    }
    return render(request, "belote/dealer.html", context)


def new_deal(request):
    if cards.d:
        cards.d.clear()
        cards.d_new = cards.Deal()
    else:
        cards.d_new.clear()
        cards.d = cards.Deal()
    return render(request, "belote/newdeal.html", {})