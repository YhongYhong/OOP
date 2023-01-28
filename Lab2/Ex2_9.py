day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_in_month2 = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
      return True
    else:
      return False

def day_of_year(day, month, year):
    days = 0
    if is_leap(year) and month > 2:
      days += 1
    for i in range(0,month):
      if i != month:
        days += day_in_month[i]
      if i == (month-1):
        days += day
    return days

def day_in_year(year):
    if is_leap(year):
      return 366
    else:
      return 365

def date_diff(date1, date2):
    sum = 0
    first = list(map(int,date1.split('-')))
    second = list(map(int,date2.split('-')))

    if (first[1]>12 or second[1]>12) or (first[1]<1 or second[1]<1): # check day
      return -1

    if is_leap(first[2]):
      day_in_month[2] = 29
    if is_leap(second[2]):
      day_in_month2[2] = 29
    if first[0] > day_in_month[first[1]] or second[0] > day_in_month2[second[1]]: # check month
      return -1

    diff1 = day_in_year(first[2]) - day_of_year(first[0],first[1],first[2]) + 1
    diff2 = day_of_year(second[0],second[1],second[2])
  
    for i in range(first[2]+1,second[2]):
      if is_leap(i):
        sum += 366
      else:
        sum += 365

    sum = sum + diff1 + diff2
    return sum

print(date_diff("28-2-2018","29-2-2020"))