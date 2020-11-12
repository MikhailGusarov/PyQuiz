from django.urls import path

from . import views

app_name = 'owngame'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_number>/', views.game, name='game'),
    path('<int:game_number>/<int:category_id>/<int:count_points>', views.question, name='question')
]
