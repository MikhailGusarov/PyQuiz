from team import Team
from question import Question


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


