# Пункт 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('Пункт 1')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Пункт 2
values_list = [3.14, 'error', True]
values_dict = {'a': 10, 'b': 20, 'c': False}
print('\nПункт 2')
print_params(*values_list)
print_params(**values_dict)

# Пункт 3
print('\nПункт 3')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
