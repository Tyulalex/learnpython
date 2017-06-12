import sys

PROF_TO_AGE_RANGE_MAP = {'Детский сад': [0, 6],
                         'Школа': [7, 16],
                         'Университет': [17, 22],
                         'Работа': [23, 69],
                         'Пенсия': [70, 120]}


def is_raw_age_valid(raw_age, max_age=120):
    if raw_age.isdigit() and int(raw_age) < max_age:
        return True


if __name__ == '__main__':
    raw_age = input("Введите ваш возраст\n")
    if not is_raw_age_valid(raw_age):
        print("Введено неправильно значение, пожалуйста, введите корректный возраст")
        sys.exit(1)
    age = int(raw_age)

    for profession, age_range in PROF_TO_AGE_RANGE_MAP.items():
        if age_range[0] <= age <= age_range[1]:
            print(profession)
            sys.exit()
    print(
        "Род занятий не определен для вашего возраста: {age}". format(
            age=age))
