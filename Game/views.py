from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})


def bonus(request):
    return render(request, "bonus.html", {})