from django.db import models
import datetime


class Game(models.Model):
    """Игра с определенным номером, как объединение вопросов"""
    number = models.PositiveIntegerField(verbose_name='Номер игры', unique=True, help_text='Введите номер игры')
    name = models.CharField(verbose_name='Название игры', max_length=300, blank=True,
                            null=True, help_text='Введите название игры')
    time = models.DateTimeField(verbose_name='Дата и время игры', blank=True,
                                null=True, help_text='Введите дату и время игры')

    class Meta:
        ordering = ["-number"]

    def __str__(self):
        if self.time is None:
            time = ''
        else:
            time = self.time.strftime("%d.%m.%Y %H:%M")

        if self.name is None:
            name = ''
        else:
            name = f'"{self.name}"'

        return f'Игра № {str(self.number)} {name} {time}'


class Category(models.Model):
    """Группа вопросов, разбитая по категориям"""
    name = models.CharField(verbose_name='Название категории', max_length=100, help_text='Введите название категории')
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             verbose_name='Игра', help_text='Выберите игру')

    def __str__(self):
        return f'{self.game}: {self.name}'


class SimpleQuestion(models.Model):
    """Обычный вопрос"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория', help_text='Выберите категорию')
    content_question = models.TextField(verbose_name='Вопрос', help_text='Введите вопрос')
    correct_answer = models.CharField(verbose_name='Ответ', max_length=200, help_text='Введите ответ')
    count_points = models.PositiveIntegerField(verbose_name='Количество очков', help_text='Введите количество очков')

    def __str__(self):
        return f'{self.category} Цена: {str(self.count_points)}'


class Team(models.Model):
    """Команда-участник"""
    name = models.CharField(verbose_name='Название команды', max_length=200, help_text='Введите название команды')
    count_points = models.PositiveIntegerField(verbose_name='Количество баллов команды', default=0)

    def __str__(self):
        return self.name


class Leading(models.Model):
    """Ведущий"""
    name = models.CharField(verbose_name='Имя', max_length=200)

    def __str__(self):
        return self.name


class Match(models.Model):
    """Конкретный матч"""
    number = models.PositiveIntegerField(verbose_name='Номер', unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    leading = models.ForeignKey(Leading, on_delete=models.CASCADE, verbose_name='Ведущий')
    date_start = models.DateTimeField(verbose_name='Время начала матча', null=True, blank=True)
    date_end = models.DateTimeField(verbose_name='Время окончания матча', null=True, blank=True)

    def __str__(self):
        return f'Матч №{str(self.number)} {self.game}'


class MatchTeam(models.Model):
    """Команды в матче"""
    play = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name='Матч')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')
    count_points = models.PositiveIntegerField(verbose_name='Очки за матч', default=0)

    def __str__(self):
        return f'Команда: {str(self.team)} Матч №{self.play.number}'


class MatchQuestion(models.Model):
    """Вопросы в матче"""
    play = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name='Матч')
    question = models.ForeignKey(SimpleQuestion, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_done = models.BooleanField(verbose_name='Отвечен', default=False)

    def __str__(self):
        return f'{self.question} Матч №{self.play.number}'
