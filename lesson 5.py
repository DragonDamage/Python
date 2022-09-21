# 1 задание:
my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()


# 2 задание:
def count_info():
    try:
        with open('new_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()


# 3 задание:
def workers_statistics():
    workers = [['Сидоров ', '12000 \n'], ['Кукушкин ', '19000 \n'], ['Иванов ', '145000 \n'], ['Смирнов ', '80000']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_statistics()


# 4 задание:
def rewrite_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('file.txt', 'r+', encoding="utf-8") as file:
            with open('new_file.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()


# 5 задание:
def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()
