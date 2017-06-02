
search_name = "Валера"



def find_person(name):
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while len(names) != 0:
        name = names.pop()
        if name == search_name:
            print("{search_name} Нашелся!".format(search_name=search_name))

if __name__ == '__main__':
    find_person(search_name)