immutable_var = True, 1, 'text', 3.14, [3, 4, 5]
print(immutable_var)
# immutable_var [0] = False # кортеж является неизменяемым типом данных
# immutable_var [1] = 2 # после того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять
immutable_var [-1] [0] = 'smth' # но поддаются изменению элементы списка, входящего в кортеж
immutable_var = immutable_var + ('text2', False) # также с кортежами можно выполнять операции конкатенации и умножения
print(immutable_var, "\n")

mutable_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(mutable_list)
mutable_list [::2] = [-1*x for x in mutable_list[::2]]
print(mutable_list)