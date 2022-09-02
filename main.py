# age = 27
# print(age)
# # целые числа - integer - int
# res = 78 / 2
# print(2 ** 3)  # возведение в степень **
# print(res)
# print(7 // 2)  # целочисленное деление
# print(7 % 2)  # остаток от деления
# sec = 1200
# print(sec // 60)  # перевели в секунды
# print(sec // 3600)  # перевели в часы
# # [Ctrl] + [Alt] + [L] - форматирование в pycharm
# # десятичное число - float
# temp = 10
# print(temp)
# print(type(temp))  # напишет тип переменной
# # строки - string - str
# name = 'Andrey'
# name2 = 'Ivan'
# print(name, name2)
# age = '50'  # сделали из int str
# print(name + ' ' + name2)  # склеить строки с пробелом
# print(name * 5)  # умножить строку 5 раз
#
# # input () - запросить у клиента, всегда превращает в строку
# age = input('enter age: ')
# print('Age:', age)
# # [Ctrl] + [Shift] + [Z] - восстановить отмененное
# # [Ctrl] + [Shift] + [/] — закомментировать/раскомментировать выделенные строки кода
#
# n1 = input('n1: ')
# n2 = input('n2: ')
# n1 = int(n1)  # инт преобразует str в int
# n2 = float(n2)  # десятичное число
# print('summ =', n1 + n2)
print(6 >= 4)
print(8 != 8)

# while - условный цикл

# проверка на правильность пароля
right = '123'
ans = input('password: ')
while ans != right:
    print('error')
    ans = input('password: ')
# while True - бесконечный цикл
# break - остановить бесконечный цикл

# счёт количества людей старше 18 и моложе 100 лет
count = 0
while True:
    print('hello')
    age = int(input('age: '))
    if age > 18:
        count = count + 1  # count += 1
    if count > 0:
        break

# находим сколько цифр в числе
n = 77777
i = 0
while n > 0:
    last = n % 10  # 123 / 10 = 12.3
    i = i + 1  # i += 1
    n = n // 10  # n //= 10
print(i, 'цифр в числе')

# проверка на возраст для прав, если 18, то езжайте, если меньше, то получите права
age = 17
if age >= 18:
    print('можете ехать')
    print('удачного пути')
else:
    print('сначала получите права')

# проверка на цвет, если есть, то принт цвет, если нет, то ничего не принт (иначе если)
color = 'red'
if color == 'red':
    print('красный')
elif color == 'green':  # else if - иначе если
    print('зеленый')
elif color == 'blue':
    print('синий')
else:
    print('такого слова нет')

# проверка возраста > 18 < 100, и age переводим в int
age = input('age: ')
age = int(age)
print(age)
if age >= 18 and age < 100:
    print('lets go')

# функция f'{переменная}' вставляем переменные в текс для удобства
age = 8
name = 'nick'
city = 'spb'
print('my age is', age, 'my name is', name, 'i live in', city)
print(f'my age is {age}. My name is {name}. I live in {city}')
