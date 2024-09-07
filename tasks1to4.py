print("1st program")
print(9**0.5*5)
print()

print("2nd program")
print(9.99 > 9.98 and 1000 != 1000.1, '\n')

print("3rd program")
print(2*2+2)
print(2*(2+2))
print(2*2+2 == 2*(2+2), '\n')

print("4th program")
some_number = '123.456'
print(int(abs(float(some_number)) * 10) % 10) # выводим первую цифру после запятой из любого положительного или отрицательного числа
print(int(abs(float(some_number)) % 1 * 10)) # второй вариант