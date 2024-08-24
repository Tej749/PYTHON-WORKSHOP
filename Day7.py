'''
Leap Year:
the leap year has 366 days. Leap year come after every 4 years
condition:
- a year divide by 400.
- a year divide by 4 but not by 100. e.g  (year % 4 == 0 and year % 100 != 0)
'''
from unittest import result


# there is two method to find leap year 1. If else condition method or user define method 2. built-in method

# Method I (if else condition method)


def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f'Yes.!! year {n}; is a leap year...!!')

    else:
        print(f"Sorry!! {n}; is not a leap year.....!")


n = int(input("Enter a Year : "))
result = is_leap(n)
print(result)