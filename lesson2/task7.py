

def ask_user():
    expected_answer = "Хорошо"
    actual_answer = ''
    while actual_answer != expected_answer:
        actual_answer = input("Как дела\n")

if __name__ == '__main__':
    ask_user()