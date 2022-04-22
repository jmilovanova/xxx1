# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 1
my_name = 'Женя'
print(my_name)

# 2
my_age = 19
print('Меня зовут', my_name + '. Мне', my_age, 'лет.')

# 3
my_name_5 = (my_name + ' ') * 5
print(my_name_5)

# 4
print('Как вас зовут?')
user_name = input()
list_user_name = list(user_name)
if ' ' in list_user_name:
    print('Введите ваше имя без пробелов.')
print('Сколько вам лет?')
user_age = input()
if 0 < int(user_age) < 150:
    print('Здравствуйте,', user_name + '! Вам', user_age + '? Не пора ли пойти отдохнуть? Устали, наверное.')
else:
    print('Введите свой настоящий возраст.')

# 5
print('Сколько вам лет?')
user_age = input()
if 0 < int(user_age) < 150:
    if int(user_age) > 60:
        print('Я думал, что в таком возрасте не умеют пользоваться компьютером...')
    elif int(user_age) < 18:
        print("А тебе мама разрешила пользоваться компьютером?")
    else:
        print('Ну раз не в возрасте дело, что тогда медлишь?')
else:
    print('Введите свой настоящий возраст.')

# 6
print(user_name[1:-1], user_name[::-1], user_name[-3:], user_name[:5], sep="\n")

# 7
user_age = list(user_age)
for i in range(len(user_age)):
    user_age[i] = int(user_age[i])
user_age_mult = 1
for i in range(len(user_age)):
    user_age_mult *= user_age[i]
print('Длина имени -', len(user_name), 'Сумма чисел возраста -', sum(user_age), 'Произведение чисел возраста -', user_age_mult)

# 8
print(user_name.upper(), user_name.lower(), user_name.capitalize(), user_name.capitalize().swapcase(), sep="\n")

# 9 проверка добавлена изначально в задании 4

# 10
print("Решите уравнение: (5x-2)/8=1")
answer = int(input())
if answer == 2:
   print("Верно.")
else:
   print("Неверно. Попробуйте снова.")


