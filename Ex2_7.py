day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

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
  
print(day_of_year(16, 10, 1966))
