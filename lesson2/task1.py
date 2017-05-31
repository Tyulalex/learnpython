import sys


def is_raw_age_valid(raw_age):
    if raw_age.isdigit() and int(raw_age) < 120:
        return True


if __name__ == '__main__':
    raw_age = input("Введите ваш возраст\n")
    if not is_raw_age_valid(raw_age):
        print("Введено неправильно значение, пожалуйста, введите корректный возраст")
        sys.exit(1)
    age = int(raw_age)
    if age < 6:
        print("Детский сад")
    elif age < 16:
        print("Школа")
    elif age < 22:
        print("Университет")
    elif age < 70:
        print("Работа")
    else:
        print("Пенсия")
