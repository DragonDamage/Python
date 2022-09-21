# 1 задание:
age = 18
name = 'andrey'
print(f'age: {age}, name: {name}')

# 2 задание:
sec = int(input('Введите время в секундах: '))
hours = sec // 3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (sec % 3600) // 60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
print(f'Формат чч:мм:сс - : {hours_res}:{minutes_res}:{seconds_res}')

# 3 задание:
n = input('Введите число: ')
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
result = n + nn + nnn
print(result)

# 4 задание:
num = int(input("Введите целое положительное число: "))
max_digit = 0  # задание начального значения наибольшей цифры
while num > 0:  # перебор цифр числа и сравнение с наибольшей
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
        if max_digit == 9:  # нет смысла, если встретилась 9
            break
    num //= 10
print(max_digit)  # выводим наибольшее число

# 5 задание:
income = int(input("Введите значение выручки: "))
outcome = int(input("Введите значение издержек: "))
profit = income - outcome  # считаем прибыль
if profit > 0:
    print("Фирма отработала с прибылью")  # если фирма получила прибыль
    profitability = profit / income  # считаем рентабельность
    print('Рентабильность составила {:.2f}'.format(profitability))
    employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / employees  # считаем прибыль на каждого сотрудника
    print('Прибыль фирмы в расчете на одного сотрудника составила {:.2f}'.format(profit_per_employee))
elif profit == 0:  # если фирма отработала в ноль
    print("Фирма отработала в ноль")
else:  # если фирма отработала в минус
    print("Фирма отработала в минус")

# 6 задание:
a = int(input("Введите результат в первый день (км): "))
b = int(input("Введите результат который нужно достигнуть (км): "))
counter = 1  # значение счетчика дней
while a < b:
    a *= 1.1  # расчет расстояния
    counter += 1  # увеличение счетчика дней
print(f"На {counter} день спортсмен достиг результата — не менее {b} км") # выводим результат
