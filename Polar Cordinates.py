import cmath
string = input()
if '+' in string:
  string = string.split("+")
  x = int(string[0])
  y = int(string[1].replace("j", ""))

elif '-' in string:
  string = string.split("-")
  if len(string) ==3:
    x = (-1)*int(string[1])
    y = (-1)*int(string[2].replace("j", ""))
  elif string[0] == '':
    x=0
    y = (-1)*int(string[1].replace("j", ""))
  else:
    x = int(string[0])
    y = (-1)*int(string[1].replace("j", ""))

elif 'j' not in string:
  x = int(string)
  y = 0

elif '+' not in string:
  x = 0
  y = int(string.replace("j", ""))

print(abs(complex(x, y)))
print(cmath.phase(complex(x, y)))
