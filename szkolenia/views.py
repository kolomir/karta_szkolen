from django.shortcuts import render
from .models import Szkolenia


def ostatnie_wpisy(request):
    ostatnie_szkolenia = Szkolenia.objects.all().order_by('-id')[:50]
    context = {
        'ostatnie_szkolenia': ostatnie_szkolenia
    }
    return render(request, 'szkolenia/ostatnie.html', context)
