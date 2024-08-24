import calendar
'''
Leap Year : The leap year has a 366 days. It comes after every 4 years.

condition :
    a.  A year divided by 400.
        eg. 2000
    b.  A yeard divided by 4 but not by 100.
        2012

'''


# Method-1 ( using if else condition.

# def is_leap(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year != 100):
#        print(f'{x}; is a leap year...!!!')
#
#     else:
#         print(f'Sorry!!! {x}; is not a leap year!!!!')
#
#
# x = int(input("Enter a Year : "))
# report = is_leap(x)
# print(report)

x = int(input("Enter a Year : "))

if calendar.isleap(x):
    print("It's a leap year..!!!")

else:
    print("Tt's not a leap year....")


