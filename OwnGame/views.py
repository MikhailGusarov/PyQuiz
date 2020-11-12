from django.shortcuts import render

from .models import Game


def index(request):
    games = Game.objects.order_by('number')
    context = {'games': games}
    return render(request, 'index.html', context)


def game(request, game_number):
    current_game = Game.objects.filter(number=game_number)
    context = {'game': current_game[0]}
    return render(request, 'game.html', context)
