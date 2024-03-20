rows = 4
columns = 5
print("Full Square Pattern")
for i in range(rows):
    for j in range(columns):
        print('*', end="")
    print()
# *****
# *****
# *****
# *****
print("Hollow Square Pattern")
side = int(input("Please Enter any Side of a Square  : "))
for i in range(side):
    for j in range(side):
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()
