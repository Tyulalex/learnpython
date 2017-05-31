



def print_age_message(age):
    if int(age) < 19:
        print('You are very young!!!')
    else:
        print('You are not young anymore....')



if __name__== '__main__':
    age = input('Enter your age: ')
    print_age_message(age)