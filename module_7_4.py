# Входные данные:
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.37451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total

# Использование %:
print('В команде "%s" участников: %s!' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})
print()

# Использование format():
print('Команда "{}" решила задач: {}!'.format(team2, score_2))
print('"{0}" решили задачи за {1:.1f} с!'.format(team2, team2_time))
print()

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')

def who_won():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team2}!'
    else:
        result = 'Ничья!'
    return result

print(who_won())
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу.')