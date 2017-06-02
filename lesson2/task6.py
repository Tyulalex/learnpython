
search_name = "Валера"

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

while len(names) != 0:
    name = names.pop()
    if name == search_name:
        print("{search_name} Нашелся!".format(search_name=search_name))

