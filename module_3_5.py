def get_multiplied_digits(number):
    str_number = str(int(number))       # cтроковое представление числа
    first = int(str_number[0])          # первый символ (цифра) из числа в строковом представлении
    if len(str_number) > 1:             # условие работы рекурсивного умножения
        return first * get_multiplied_digits(int(str_number[1:])) # умножение первой цифры числа на результат работы этой же функции с числом, но уже без первой цифры
    else:
        return first # возврат числа из одной цифры


result = get_multiplied_digits(40203)
print(result)
