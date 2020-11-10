class Team:
    """Команда-участник"""
    name = ''
    count_points = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Question:
    """Вопрос"""
    content_question = ''
    correct_answer = ''
    count_points = 0

    def __init__(self, content_question, correct_answer, count_point):
        self.content_question = content_question
        self.correct_answer = correct_answer
        self.count_points = count_point

    def __str__(self):
        return self.content_question


questions = [Question('Сколько будет 2+2', '4', 1),
             Question('Если рыба-меч с острым носом, то птица с острым клювом - это?', 'жаба', 5),
             Question('Я ему сын сына, а он мне', 'дед', 3),
             Question('Острая кувалда', 'секира', 2),
             ]

teams = []

print('Добро пожаловать в игру "Викторина"')
count_teams = input('Введите количество команд: ')

for i in range(int(count_teams)):
    team_name = input('Введите название команды: ')
    teams.append(Team(team_name))


for questions in questions:
    print(questions)