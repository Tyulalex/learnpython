def get_summ(something, something_else):
    return '{something}{something_else}'.format(something=something, something_else=something_else).upper()


if __name__=='__main__':
    print(get_summ('Hello', 2))