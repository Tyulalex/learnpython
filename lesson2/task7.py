

def ask_user():
    expected_answer = "Хорошо"
    actual_answer = ''
    while actual_answer != expected_answer:
        actual_answer = input("Как дела\n")
        return actual_answer


def get_answer():
    expected_answer = "Пока"
    actual_answer = ''
    while actual_answer != expected_answer:
        actual_answer = ask_user()

if __name__ == '__main__':
    get_answer()