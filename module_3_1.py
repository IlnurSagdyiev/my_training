calls = 0


def count_calls():  # функция подсчета количества вхождений остальных функций
    global calls    # обращаемся к глобальной переменной
    calls += 1      # увеличиваем на 1 в случае применения функции
    return calls    # возвращаем количество


def string_info(string):            # ф-я возвращающая кортеж из длины строки, строки в верхнем регистре, строки в нижнем регистре
    total_characters = len(string)  # подсчитываем количество символов
    upper_case = string.upper()     # переводим в верхний регистр
    lower_case = string.lower()     # переводим в нижний регистр
    count_calls()                   # применяем счетчик
    return total_characters, upper_case, lower_case # реализовываем логику работы по описанию


def is_contains(string, list_to_search):                # ф-я проверки вхождения слова в список без учета регистра
    is_cont = True                                      # вводим булеву переменную (флаг)
    for i in range(len(list_to_search)):                # перебираем список
        if string.lower() == list_to_search[i].lower(): # проверка равенства слова с элементами списка
            is_cont = True                              # если вхождение найдено, обозначаем с помощью переменной флага и
            break                                       # дальнейший поиск не требуется
        else:                   # если вхождение не найдено, обозначаем с помощью переменной флага как False
            is_cont = False
    count_calls()               # применяем счетчик
    return is_cont              # выводим информацию о вхождении слова в список


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('UrBaN', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
