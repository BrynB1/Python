# month_days_v2.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
month = input("Enter a 3 letter month abbreviation with all lower case: ")
if month == "feb":
    leapyear = input("Is it a leap year? (y or n):")
    if leapyear == "y":
        days = 29
    if leapyear == "n":
        days = 28
elif month == "jan" or month == "mar" or month == "may" or month == "jul" or \
   month == "aug" or month == "oct" or month == "dec":
    days = 31
elif month == "apr" or month == "jun" or month == "sep" or month == "nov":
    days = 30
else:
    print("Invalid month")
    days = -1
print("Number of days in month:", days)
