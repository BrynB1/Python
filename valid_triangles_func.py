# valid_triangles_func.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def main():
    print("Valid Triangle?", valid_triangles())
    repeat()


def valid_triangles():
    side1, side2, side3 = input("Please enter the 3 integer edges of a triangle(separated by a space):").split()
    if side1 + side2 > side3 or side2 + side3 > side1 or side3 + side1 > side2:
        return True
    else:
        return False


def repeat():
    redo = str(input("Enter 'yes' if you would like to do another calculation:"))
    if redo == 'yes':
        main()
    else:
        pass


main()
