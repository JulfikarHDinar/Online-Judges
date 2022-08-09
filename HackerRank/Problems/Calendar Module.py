import calendar
#weekday(year, month, day)
inputDate = input().split()
month = int(inputDate[0])
day = int(inputDate[1])
year = int(inputDate[2])

temp = calendar.weekday(year, month, day)

if temp == 0:
  print("MONDAY")
elif temp == 1:
  print("TUESDAY")
elif temp == 2:
  print("WEDNESDAY")
elif temp == 3:
  print("THURSDAY")
elif temp == 4:
  print("FRIDAY")
elif temp == 5:
  print("SATURDAY")
elif temp == 6:
  print("SUNDAY")
