from django.shortcuts import render

def hero(request):
    return render(request, 'hero.html')