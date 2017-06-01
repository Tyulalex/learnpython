import sys

def foo(string1, string2):
    if string1 == string2:
        return 1
    else:
        if len(string1) > len(string2):
            return 2
        elif string2 == 'learn':
            return 3
        else:
            return 'None'

if __name__=='__main__':
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    print(foo(string1, string2))