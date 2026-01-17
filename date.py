def is_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def day_of_year(day, month, year):
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        day_in_month[1] = 29

    day_of_year = sum(day_in_month[:month - 1]) + day
    return day_of_year

def day_in_year(year):
    return 366 if is_leap(year) else 365

def date_diff(date1, date2):
    d1, m1, y1 = map(int, date1.split('-'))
    d2, m2, y2 = map(int, date2.split('-'))

    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1
    days = day_in_year(y1) - day_of_year(d1, m1, y1) + 1

    for year in range(y1 + 1, y2):
        days += day_in_year(year)

    days += day_of_year(d2, m2, y2)


    return days

input_date1 = input("Enter the first date (DD-MM-YYYY): ")
input_date2 = input("Enter the second date (DD-MM-YYYY): ")

print(date_diff(input_date1, input_date2))
print(is_leap(2020))  # Example usage of is_leap function
print(day_of_year(1, 3, 2020))  # Example usage of\
