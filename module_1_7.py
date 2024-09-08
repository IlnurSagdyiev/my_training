# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Решение
students = list(students) # преобразовываем множество в список
students.sort() # сортируем по алфавиту
average_grades = [sum(x) / len(x) for x in grades] # создаем список усредненных оценок
academic_progress_register = dict(zip(students, average_grades)) # создаем словарик совмещая два отсортированных списка
print(academic_progress_register)
