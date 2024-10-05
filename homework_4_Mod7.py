# Домашнее задание по теме "Форматирование строк"
from faulthandler import dump_traceback

team_name1 = 'Мастера кода'
team_name2 = 'Волшебники Данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = float(1552.512)
team2_time = float(2153.31451)
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1) # 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team_name1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team_name2}!'
else:
    challenge_result = 'Ничья!'

print('Команда %s: %s участников' % (team_name1, team1_num))
print('Команда %s: %s участников' % (team_name2, team2_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

print('Командой {}'.format(team_name1), 'решено: {}'.format(score_1), 'задач')
print('Командой {}'.format(team_name2), 'решено: {}'.format(score_2), 'задачи')
print('Счёт: {}:{}'.format(score_1, score_2))
print('Команда {}'.format(team_name1), 'решили задачи за {}'.format(team1_time), 'секунды')
print('Команда {}'.format(team_name2), 'решили задачи за {}'.format(team2_time), 'секунду')

print(f'Количество решённых задач: {tasks_total}')
print(f'Среднее время выполнения задачи: {time_avg} секунды')
print(f'Результат выполнения задания: {challenge_result}')
