# CS175L-01
# Bryn Bijur
# calc_average

def main():
    calc_average()
    repeat()


def determine_grade(grade):
    if 90 <= grade <= 100:
        letter_grade = "A"
    elif 80 <= grade <= 89:
        letter_grade = "B"
    elif 70 <= grade <= 79:
        letter_grade = "C"
    elif 60 <= grade <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def my_random(grade):
    import random
    grade = random.randint(1, 100)
    return grade


def calc_average():
    count = 1
    grade = 0
    grade1 = my_random(grade)
    grade2 = my_random(grade)
    grade3 = my_random(grade)
    grade4 = my_random(grade)
    grade5 = my_random(grade)
    letters1 = determine_grade(grade1)
    letters2 = determine_grade(grade2)
    letters3 = determine_grade(grade3)
    letters4 = determine_grade(grade4)
    letters5 = determine_grade(grade5)
    print("Score\tNumeric Grade\tLetter Grade")
    print("__________________________________")
    print("Score", count, ":\t", grade1, "\t\t", letters1)
    count = count + 1
    print("Score", count, ":\t", grade2, "\t\t", letters2)
    count = count + 1
    print("Score", count, ":\t", grade3, "\t\t", letters3)
    count = count + 1
    print("Score", count, ":\t", grade4, "\t\t", letters4)
    count = count + 1
    print("Score", count, ":\t", grade5, "\t\t", letters5)
    total = grade1 + grade2 + grade3 + grade4 + grade5
    average = total / count
    print("Average =", average)
    return count


def repeat():
    redo = str(input("Enter 'yes' if you would like to do another calculation:"))
    if redo == 'yes':
        main()
    else:
        pass


main()
