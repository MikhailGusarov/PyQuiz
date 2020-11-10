class Team:
    """Команда-участник"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Question:
    """Вопрос"""
    def __init__(self, content_question, correct_answer, count_point):
        self.content_question = content_question
        self.correct_answer = correct_answer
        self.count_points = count_point

    def __str__(self):
        return self.count_point


class Category:
    """Категория вопросов"""
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __str__(self):
        return self.name


questions_category = [Question('Сколько будет 2+2', '4', 1),
                      Question('Если рыба-меч с острым носом, то птица с острым клювом - это?', 'жаба', 5),
                      Question('Я ему сын сына, а он мне', 'дед', 3),
                      Question('Острая кувалда', 'секира', 2)]

test_category = Category('Просто котегория', questions_category)

teams = []

print('Добро пожаловать в игру "Викторина"')
count_teams = input('Введите количество команд: ')

for i in range(int(count_teams)):
    team_name = input('Введите название команды: ')
    teams.append(Team(team_name))


