from django.shortcuts import get_object_or_404, render

from .models import Game, Question


def index(request):
    games = Game.objects.order_by('number')
    context = {'games': games}
    return render(request, 'index.html', context)


def game(request, game_number):
    current_game = get_object_or_404(Game, number=game_number)
    context = {'game': current_game}
    return render(request, 'game.html', context)


def question(request, game_number, id_category, count_points):
    current_question = get_object_or_404(Question, count_points=count_points, category=id_category)
    context = {'question': current_question}
    return render(request, 'question.html', context)
