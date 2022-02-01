#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1, 6):
    print(i, '0000000000000000000000000000000000000000000')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
count = 0

for i in range(10):
    user_data = int(input('Введите число: '))
    if user_data == 5:
        count += 1
print(count)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1, 101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
proiz = 1

for i in range(2, 11):
    proiz *= i
print(proiz)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
integer_number = 123456

start_del = len(str(integer_number)) - 1
delitel = 10 ** start_del

#print(integer_number % delitel, integer_number // delitel)

while integer_number > 0:
    print(int(integer_number // delitel))
    integer_number = integer_number % delitel
    delitel /= 10

'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = 123456
sum = 0

while integer_number > 0:
    sum += integer_number % 10
    integer_number = integer_number // 10

print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = 123456
proiz = 1

while integer_number > 0:
    proiz *= integer_number % 10
    integer_number = integer_number // 10

print(proiz)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 125254

while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else:
    print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number = 125278954
max_num = integer_number % 10

while integer_number > 0:
    max_num = max(max_num, integer_number % 10)
    integer_number = integer_number // 10

print(max_num)
'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 125278954
count_num = 0

while integer_number > 0:
    if integer_number % 10 == 5:
        count_num += 1
    integer_number = integer_number // 10

print(count_num)


