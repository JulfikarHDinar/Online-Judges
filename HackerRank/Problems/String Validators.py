if __name__ == '__main__':
    s = input()
    list1 = list(s)
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False

    for i in list1:  
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
        if i.isdigit():
            digits = True
        if i.isalpha():
            alphabetical = True
        if i.isalnum():
            alphanumeric = True

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
