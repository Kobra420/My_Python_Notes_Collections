def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_name = "January Frbruary March April May June July August September October November December"
    month_name_lst = month_name.split(' ')
    if is_leap(year) and month == 2:
        print(f"{month_name_lst[month-1]}")
        return 29
    print(f"{month_name_lst[month-1]}")
    return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
