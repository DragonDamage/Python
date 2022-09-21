# 1 задание:
type_list = [9, 5 / 6, True, [1, 2], "Hi", {"books": "Sherlok", "Author": "KonanDoyle"}, (1, 2)]
for i in range(len(type_list)):
    print(f"Тип переменной в списке: {type(type_list[i])}")

# 2 задание:
q = int(input("How many items in list do you want to add?\n\t Enter items quantity: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Item # {i + 1} : "))
print(f"Your item list view:\n{my_lst}")
for x in range(0, (len(my_lst) - 1), 2):
    my_lst[x], my_lst[x + 1] = my_lst[x + 1], my_lst[x]
print(f"Your CHANGED item list view:\n{my_lst}")

# 3 задание:
# 1 решение
month = int(input("Please enter month id from 1 to 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0:
        print(f"\tINCORRECT ID!!! \n\tPlease use number range from 1 to 12 only!")
        month = int(input("Please enter month id from 1 to 12 : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tSeason related to your Month id#{month}  is '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tSeason related to your Month id# {month} is '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tSeason related to your Month id# {month} is '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tSeason related to your Month id# {month} is '{mlist[3]}'")
        break
# 2 решение
seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
months_dict = {1: seasons.get(1), 2: seasons.get(1), 3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
               6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3), 9: seasons.get(4), 10: seasons.get(4),
               11: seasons.get(4), 12: seasons.get(1)}
value = months_dict[month] if month in months_dict else print(f"Your month id {month} is not found in seasons")
print(f"\tSearch result in seasons dictionary for month id# {month} is:  '{value}'")

# 4 задание:
text = input("Please type your text : ")
T = text.split()
for x, y in enumerate(T, start=1):
    if len(y) > 11:
        y = y[:10]
        print(x, y)
    else:
        print(x, y)

# 5 задание:
rate_list = [7, 5, 3, 3, 2]
frq = int(input("How many rates do you want to add?\n\t ENTER QUANTITY: "))
for j in range(frq):
    add_new = int(input("What's rate do you want to add?\n\t ENTER RATE: "))
    if add_new in rate_list:
        i = rate_list.index(add_new)
        while (i + 1) <= (len(rate_list) - 1) and (rate_list[i] == rate_list[i + 1]):
            i += 1
        rate_list.insert(i, add_new)
        print(f"Updated rate_list {rate_list}")
    else:
        if add_new <= rate_list[-1]:
            rate_list.append(add_new)
            print(f"Updated rate_list {rate_list}")
        else:
            rate_list.insert(0, add_new)
            print(f"Updated rate_list {rate_list}")

# 6 задание:
q = int(input("Здравствуйте! Сколько продуктов желаете добавить в систему?\n\t Кол-во: "))
chr = "Название", "Цена", "Количество", "Ед.изм"
products, names, prices, Quantity, uoms = [], [], [], [], []
for i in range(q):
    print(f"Введите характеристики для товара # {i + 1} :")
    name, price, quantity, uom = input("\tНазвание : "), input("\tЦена товара : "), input("\tКоличество : "), \
                                 input("\tЕд.изм : ")
    products_up = (i + 1, {chr[0]: name, chr[1]: price, chr[2]: quantity, chr[3]: uom})
    products.append(products_up)
    names.append(products[i][1].get(chr[0]))
    prices.append(products[i][1].get(chr[1]))
    Quantity.append(products[i][1].get(chr[2]))
    uoms.append(products[i][1].get(chr[3]))
analytics = {chr[0]: names, chr[1]: prices, chr[2]: Quantity, chr[3]: uoms}
print(f"Статистика по товарам ниже \n{analytics}")
