from django.shortcuts import render
from belote import cards, forms

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
    if request.method == 'POST':
        form = forms.PlayerForm(request.POST)

        if form.is_valid():
            cards.p1 = form.cleaned_data["player1_name"]
            cards.p2 = form.cleaned_data["player2_name"]
            cards.p3 = form.cleaned_data["player3_name"]
            cards.p4 = form.cleaned_data["player4_name"]
    else:
        form = forms.PlayerForm()

    context = {
        "form": form,
    }
    return render(request, "belote/newdeal.html", context)
