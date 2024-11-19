def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        class_of_number = f'{res} - ни простое, ни составное'
        if res > 1:
            for i in range(2, res):
                if res % i == 0:
                    class_of_number = f'{res} - составное'
                    break
                else:
                    class_of_number = f'{res} - простое'
        return class_of_number
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(0, 0, 1)
print(result)
result2 = sum_three(2, 3, 6)
print(result2)
result3 = sum_three(1, 2, 3)
print(result3)