from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def kontant_view(request):
    return render(request, 'kontakt.html')

def ziele_view(request):
    return render(request, 'ziele.html')
