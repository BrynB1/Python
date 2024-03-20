def main():
    print("The second largest number is:", second_largest())
    repeat()


def second_largest():
    num1, num2, num3 = input("Please enter 3 numbers:").split()
    if num2 < num1 < num3:
        return num1
    if num1 < num2 < num3:
        return num2
    if num1 < num3 < num2:
        return num3


def repeat():
    redo = str(input("Enter 'yes' if you would like to run the program again:"))
    if redo == 'yes':
        main()
    else:
        pass


main()
