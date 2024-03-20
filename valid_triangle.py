#valid_triangle.py
#Bryn Bijur, s1324044
#CS-175
#Spring 2022

#Input
a = int(input("Enter the first integer edge of a triangle:"))
b = int(input("Enter the second integer edge of a triangle:"))
c = int(input("Enter the third integer edge of a triangle:"))
#Output
if a + b > c and b+c>a and c+a>b:
    print("Valid triangle? YES")
else:
    print("Valid triangle? NO")
