import sys

def validate_input(input_value):
    if not input_value.isalpha():
        print('Incorrect value has been entered, only letters are allowed')
        sys.exit()
    if len(input_value)>30:
        print('Too long name, max 30')
        sys.exit()


def is_name_valid(raw_name, max_name_length=30):
    return not(not raw_name.isalpha() or len(raw_name) > max_name_length)

def validate_name(raw_name, max_name_length=30):
    errors = []
    if not input_value.isalpha():
        errors.append('Incorrect value has been entered, only letters are allowed')
    if len(input_value)>30:
        errors.append('Too long name, max 30')
    return errors

if __name__=='__main__':
    user_info = {'first_name':'', 
            'last_name':''
            }

    first_name = input('Enter first name: ')
#   validate_input(first_name)

    if not is_name_valid(first_name):
        sys.exit('wrong first name')

    errors = validate_name(first_name)
    if errors:
        print(errors)
        sys.exit()

    last_name = input('Enter last name: ')
    validate_input(last_name)

    
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    print(user_info)