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


class Question(models.Model):
    """Вопрос"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория', help_text='Выберите категорию')
    content_question = models.TextField(verbose_name='Вопрос', help_text='Введите вопрос')
    correct_answer = models.CharField(verbose_name='Ответ', max_length=200, help_text='Введите ответ')
    count_points = models.PositiveIntegerField(verbose_name='Количество очков', help_text='Введите количество очков')

    def __str__(self):
        return f'{self.category} Цена: {str(self.count_points)}'
