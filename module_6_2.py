class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def __get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.__get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color = str(new_color).upper()
        self.__COLOR_VARIANTS = [i.upper() for i in self.__COLOR_VARIANTS]
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()
print()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print()

# Создаем объект класса Sedan
sedan1 = Sedan('Aleks', 'Honda Accord', 240, 'Red')
sedan1.print_info()
print()
sedan1.set_color('white')
sedan1.owner = 'Maks'
sedan1.print_info()

print(dir(vehicle1))
print(dir(sedan1))

print(sedan1._Vehicle__color)