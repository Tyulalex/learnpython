import re


def count_words():
    wordcount = 0
    with open('text.txt', 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.strip()
            if line:
                line_elements = line.split()
                for word in line_elements:
                    if not is_word_not_contain_digit_and_line_folding(word):
                        wordcount += 1
    print("Total word amount: {0}".format(wordcount))


def is_word_contains_digits(word):
    return re.search('\d', word)

def is_word_ends_with_line_folding(word):
    return word.endswith('-')

def is_word_not_contain_digit_and_line_folding(word):
    return is_word_contains_digits(word) or is_word_ends_with_line_folding(word)



#обработать числа
#перенос строк
#слова могут разделяться не только пробелами, длинный пробел, табуляция
#три пробела подряд

if __name__ == '__main__':
    count_words()



