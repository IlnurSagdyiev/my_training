my_dict = {'Timur': 1985, 'Alexei': 1987, 'Valentina': 1992, 'Alexander': 1986}
print('Словарь: ', my_dict)
print('Alexander ', my_dict['Alexander'])
print('Anton ', my_dict.get('Anton', 'Такого сотрудника нет'))

# employee = input()
# print(employee, my_dict.get(employee, 'Такого сотрудника нет'))

my_dict['Vika'] = 1989
my_dict.setdefault('Maksim', 1994)
print('\nДобавили сотрудников:', my_dict)
a1 = my_dict.pop('Timur')
print('\nИвлеченное значение:', a1)
print(my_dict, '\n')

my_set = {'a', 'b', 3, 'c', 2, 'a', 2, 0}
print(f'Множество: {my_set}')

my_set.add((True, False))
print('Добавили кортеж:', my_set)

my_set2 = {2, 5, 'a', 'd'}
my_set = my_set.union(my_set2)
print('В коллекцию my_set добавили значения множества my_set2:\n', my_set)

my_set.remove('a')
print("\nУдалили элемент 'a' из множества my_set:", my_set)

