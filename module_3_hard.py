data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args, **kwargs):
    data_ = []  # собираем список из всех переменных
    for i in args:
        data_.append(i)
    for i in kwargs.items():
        data_.append(i)
    summa_ = 0  # создаем переменную для подсчета суммы
    for i in data_:  # перебираем собранный из переменных список
        if isinstance(i, int) or isinstance(i, float):   # суммируем числовые значения
            summa_ += i
        elif isinstance(i, str):  # подсчет строковых символов
            summa_ += len(i)
        elif isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):   # пробегаемся по вложенным коллекциям с рекурсией
            for j in i:
                summa_ += calculate_structure_sum(j)
        elif isinstance(i, dict):   # пробегаемся по вложенным словарям с рекурсией
            for j in i.items():
                summa_ += calculate_structure_sum(j)
    return summa_


result = calculate_structure_sum(data_structure)
print(result)
result2 = calculate_structure_sum(data_structure, а=4)
print(result2)
