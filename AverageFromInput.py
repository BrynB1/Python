# CS175L-01
# Bryn Bijur
# AverageFromInput.py
import sys


def main():
    try:
        total = 0
        count = 0
        file = open("numbers.txt", "r")
        for line in file:
            lines = float(line)
            total += lines
            count += 1
            print("I read in", count, "number(s) Current number is:", lines, "Total is:", total)
        average = total / count
        print("Average:", average)
    except IOError:
        print('An error occurred trying to open the file.')
        sys.exit()
    except ValueError:
        print('Non-numeric data found in the file.Skipping..')
        average = total / count
        print("Average:", average)
        sys.exit()


# Call the main function.
if __name__ == '__main__':
    main()
