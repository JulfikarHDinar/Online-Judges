def timeConversion(s):
    #print(s[:2])    #hour
    #print(s[-2:])   #AM or PM
    #print(s[2:-2])  #rest string

    hour = s[:2]
    if s[-2:] == 'AM':
        if hour == '12':
            hour = '00'
    elif s[-2:] == 'PM':
        if hour == '12':
            pass
        else:
            hour = str(int(s[:2])+12)

    print(hour+s[2:-2])

if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)

#07:05:45PM
#12:05:45AM
