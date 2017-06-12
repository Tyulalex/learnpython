import csv


def write_to_csv_file(headers, dict_rows, delimiter=';'):
    with open('text.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, headers, delimiter=delimiter)
        writer.writeheader()
        for key, value in dict_rows.items():
            writer.writerow({headers[0]: key, headers[1]: value})


if __name__ == '__main__':
    headers = ['question', 'answer']
    answers = {'Как дела?': 'хорошо',
               'Как зовут?': 'Маша',
               'Что ты делала сегодня?': 'ничего'}

    write_to_csv_file(headers, answers)