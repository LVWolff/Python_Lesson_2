
print("Загадайте любое число от 1 до 100")

control_level = 50
min_level = 1
max_level = 100

while True:
    answer = input("Загаданное число больше " + str(control_level) + " (y/n)?")
    if answer == 'y':
        min_level = control_level+1
        max_level = max_level
        control_level = int((min_level + max_level) / 2)
    else:
        min_level = min_level
        max_level = control_level
        control_level = int((min_level + max_level) / 2)

    if min_level == max_level:
        print("Загаданное число:", min_level)
        break

