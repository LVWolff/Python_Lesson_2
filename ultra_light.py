
# определение функциии
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


# строковая переменная путем ввода данных
temp_var_1 = input('Input something!')

print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_var_2 = input('Input something again!')

print(temp_var_2, type(temp_var_2), id(temp_var_2))

# преобразование строки к целочисленному типу
temp_var_1 = int(temp_var_2)

print(temp_var_1, type(temp_var_1), id(temp_var_1))

# Приведение типов

temp_float = input('Input float number!')
print(temp_float, type(temp_float), id(temp_float))


if is_digit(temp_float):
    temp_float = float(temp_float)
    print(temp_float, type(temp_float), id(temp_float))
else:
    print('There is not number!')


# Типы переменных---------
#-------------------------

# Марка
# строка
name = 'Ford'

print(name, type(name))

# Возраст целое число
age = 3

print(age, type(age))

# Объем двигателя

# дробное число
engine_volume = 1.6

print(engine_volume,type(engine_volume))

# Есть ли люк?

# тип булево: истина или ложь
see_sky = False

print(see_sky, type(see_sky))


# Математические операции---------
#---------------------------------

a = input('First number')  # ввод строки первый операнд
b = input('Second number') # ввод строки второй операнд
a = int(a) # преобразование строки первого операнда к целочисленному типу
b = int(b) # преобразование строки второго операнда к целочисленному типу
print(a + b)  # сложение. для строк это конценация (объединение)
print(a - b)  # вычетание
print(a * b)  # умножение
result = a / b # деление
print(type(result))    # вывод типа результата
print(result)  # вывод результата
print(a ** 2) # вывод результата возведение в степень - в данном случае в квадрат

# Логические операции
a = True
b = False

# Отрицание
print(not a)  # инвертирование типа булево
# Логическое И
print(a and b) # проверка выполнения сразу 2-х условий
# логическое ИЛИ
print(a or b) # проверка выполнения любого из 2-х условий


a = 10 # присваивание значения
print(a > 100)   # проверка на больше
print(a < 100)   # проверка на меньше
print(a <= 100)  # проверка на меньше или равно
print(a >= 100)  # проверка на больше или равно
print(a == 100)  # проверка на "равно"
print(a != 100)  # проверка на "не равно"


# Ввод, вывод, комментарии---------
#----------------------------------


# однострочный комментарий

'''
первая строка
вторая строка
...
'''

# Вывод----------------------------
print('Hello!')
print('Hello!', 'Student!', 123)

print('Hello!', 'Student!', 123, sep = 'xxx')

print('Hello!', 'Student!', 123, end = 'yyy')

print()


# Ввод-----------------------------

age = input('Input your age')  # вводимые данные имеют тип string (строка)

print(age, type(age))
print(int(age), type(int(age)))


# Оператор условия---------
#--------------------------

brand = 'Volvo'      # бренд
engine_volume = 1.5  # объем двигателя
horsepower = 152     # мощность двигателя
sunroof = True      # наличие люка

# Проверка условия if

if horsepower < 80:
    print('No Tax')


# Проверка условия if/else
if horsepower < 80:
    print('No Tax')
else:
    print('Tax')


# Проверка условия if/elif/elif/else

tax = 0
if horsepower < 80:
    tax = 0
elif  horsepower < 100:
    tax = 10000
elif  horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)

# Проверка условия if для присваивания

cool_car = 0

cool_car = 1 if sunroof == 1 else 0

print(cool_car)


# Цикл for --------------
#--------------------------


# Простейший for
for i in range(10): # range(start, stop, step) конец границы (stop - 1)
    print(i)
    if i == 5:
        break # принудительный выход из цикла

for i in range(10):  # диапозон от 0 до 9 включительно
    answer = input('Какая лучшая марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы!')
        break # принудительный выход из цикла

for i in range(10):
    if i == 9:
        break # принудительный выход из цикла
    if i < 3:
        continue # принудительный переход к следующей итерации
    else:
        print(i)

# Цикл while --------------
#--------------------------


# Простейший while
i = 0

while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        break # принудительный выход из цикла

answer = None

while answer != 'Volvo':
    answer = input('Какая лучшая марка автомобиля?')
print('Вы абсолютно правы!')


while i < 10:
    if i == 9:
        break # принудительный выход из цикла
    if i <3:
        continue # принудительный переход к следующей итерации
    print(i)
    i = i + 1
