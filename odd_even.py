#odd_even.py
#Bryn Bijur, s1324044
#CS-175
#Spring 2022

#Input
x = int(input("Enter an integer: "))
        
#Output
if(x % 2) == 0 and (x != 0):
    print(x,"is an even number.")
elif(x % 2)!= 0:
    print(x,"is an odd number.")
else:
    print ("You entered zero.")
