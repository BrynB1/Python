# CS-175LAB
# Jarek Torres
# Bestsellers Project
# import csv

from calendar import month


def main():
    books = []
    best_sellers_file = open("bestsellers.txt", "r")
    for line in best_sellers_file:
        line = line.strip().split('\t')
        books.append(line)

    run = False

    while run == False:
        show_menu()
        choice = input("")
        if choice == str(1):  # look up year range
            yearRange(books)
        elif choice == str(2):  # look up month/year
            month_year(books)
        elif choice == str(3):  # search for author
            search_author(books)
        elif choice == str(4):  # search for title
            search_title(books)
        elif choice == "Q" or choice == "q":
            run = True
            break
        else:
            print("Please select 1-4 or Q to quit")


def yearRange(books):
    start_year = int(input("Enter start year: "))
    end_year = int(input("Enter end year: "))

    for line in books:
        date = line[3].split('/')
        year = int(date[2])
        if year >= start_year and year <= end_year:
            print(line[0], "by:", line[1], "( pub date:", line[3], ")")


def month_year(books):
    specific_month = int(input("Enter month(1-12): "))
    specific_year = int(input("Enter year: "))

    for line in books:
        date = line[3].split('/')
        year = int(date[2])
        month = int(date[0])

        if month >= specific_month >= month:
            if year >= specific_year >= year:
                print(line[0], "by:", line[1], "(pub date:", line[3], ")")


def search_author(books):
    author = input("Enter search string: ")

    for line in books:
        art = line[1]
        if art == author:
            print(line[0], "by:", line[1], "(pub date:", line[3], ")")


def search_title(books):
    title = input("Enter search string: ")
    for line in books:
        title2 = books[0]
        title3 = str(title2)
        if title3 >= title <= title3:
            print(line[0], "by:", line[1], "(pub date:", line[3], ")")


def show_menu():
    print()  # space
    print("Read 1138 books")  # read amount of books/lines
    print("What would you like to do?")
    print("\t 1: Look up year range")
    print("\t 2: Look up month/year")
    print("\t 3: Search for author")
    print("\t 4: Search for title")
    print("\t Q: Quit")


main()


