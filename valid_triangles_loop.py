# valid_triangles_loop.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
repeat = True
while repeat == True:
    a, b, c = input("Please enter the 3 integer edges of a triangle(or -1, -1, -1 to quit):").split()
    if a == "-1" or b == "-1" or c == "-1":
        repeat = False
    elif a + b > c or b + c > a or c + a > b and repeat == True:
        print("Valid triangle? YES")
    else:
        print("Valid triangle? NO")
