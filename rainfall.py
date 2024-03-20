# CS175
# Bryn Bijur
# rainfall.py
numberofyears = int(input("Enter the number of years: "))
months = 12
totalmonths = 0
totalyears = 0
for years in range (0, numberofyears):
    totalyears += 1
    print("For year",totalyears)
    for month in range(1,13):
        rainfallbymonth = float(input("Enter the rainfall amount for the month:"))
        totalmonths += rainfallbymonth
numberofmonths = numberofyears*months
average = totalmonths / numberofmonths
print("There were a total of",totalyears," year(s)")
print("There were", numberofmonths,"months")
print("The total rainfall was ", totalmonths)
print("The average monthly rainfall was", average)
                            
