import re

def pangrams(s):
    if len(set(s)) == 26:
        print('pangram')
    else:
        print('not pangram')

if __name__ == '__main__':
    s = input().lower()
    s = s.replace(' ','')
    result = pangrams(s)
