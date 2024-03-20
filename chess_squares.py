def main():
    print("That square's color is", chess_square())
    repeat()


def chess_square():
    letter = input("Input the square's letter:")
    number = int(input("Input the square's number:"))
    if letter == "a" or "c" or "e" or "g":
        if (number % 2) != 0:
            return "dark"
        else:
            return "light"
    else:
        if (number % 2) == 0:
            return "dark"
        else:
            return "light"


def repeat():
    redo = str(input("Enter 'yes' if you would like to run the program again:"))
    if redo == 'yes':
        main()
    else:
        pass


main()

