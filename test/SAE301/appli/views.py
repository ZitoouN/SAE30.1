from django.shortcuts import render

# Create your views here.

def accueil(request):
    tmplate = "base.html"
    return render(request, 'appli/base.html')

def home(request):
    return render(request, "appli/home.html")

def light1(request):
    return render(request, "appli/light1.html")

def light2(request):
    return render(request, "appli/light2.html")

def lights(request):
    return render(request, "appli/lights.html")

def temp(request):
    return render(request, "appli/temp.html")

def etat1(request):
    return render(request, "appli/etat1.html")

def etat2(request):
    return render(request, "appli/etat2.html")