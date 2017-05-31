

def get_answers(question):
    answers = {"привет": "И тебе привет!",
               "как дела": "Лучше всех",
               "пока": "Увидимся"}
    return answers.get(question.lower())

if __name__ == '__main__':
    question = input('\n')
    print(get_answers(question))