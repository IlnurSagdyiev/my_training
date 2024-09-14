def get_matrix(n, m, value):            # создаем функцию с тремя параметрами
    matrix = []                         # создаем пустой список
    for i in range(n):
        matrix.append([])               # добавляем пустые списки в количестве равном n (число строк)
        for j in range(m):              # добавляем столбцы в количестве равном m
            matrix[i].append(value)     # построчно вносим значения m раз
    return matrix                       # возвращаем матрицу


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)