class Team:
    """Команда-участник"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class SimpleQuestion:
    """Вопрос"""
    def __init__(self, content_question, correct_answer, count_point):
        self.content_question = content_question
        self.correct_answer = correct_answer
        self.count_points = count_point

    def __str__(self):
        return self.count_points


class Category:
    """Группа вопросов, разбитая по категориям"""
    def __init__(self, name, questions=None):
        if questions is None:
            questions = []
        self.name = name
        self.questions = questions

    def __str__(self):
        return self.name


class Game:
    """Игра, как сущность объединения групп вопросов"""
    def __init__(self, game_number, categories=None, date=None):
        if categories is None:
            categories = []
        self.game_number = game_number
        self.categories = categories
        self.date = date


questions_category = [SimpleQuestion('Сколько будет 2+2', '4', 1),
                      SimpleQuestion('Если рыба-меч с острым носом, то птица с острым клювом - это?', 'жаба', 5),
                      SimpleQuestion('Я ему сын сына, а он мне', 'дед', 3),
                      SimpleQuestion('Острая кувалда', 'секира', 2)]

test_category = Category('Просто котегория', questions_category)
game = Game(1, [test_category])

teams = []

print('Добро пожаловать в игру "Викторина"')
count_teams = input('Введите количество команд: ')

for _ in range(int(count_teams)):
    team_name = input('Введите название команды: ')
    teams.append(Team(team_name))

print("Выберите категорию:")
for i, category in enumerate(game.categories):
    print(i+1, category)
current_category = game.categories[int(input("Введите номер картегории: ")) - 1]
