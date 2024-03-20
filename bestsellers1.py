def main():
    books = []
    best_sellers_file = open("bestsellers.txt", "r")
    count = 0
    for line in best_sellers_file.readlines():
        line = line.strip('\n')
        cols = line.split("\t")
        books.append(cols)
        count = count + 1
    run = False
    while not run:
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
        else:
            if choice == "Q" or choice == "q":
                run = True


def showBooks(books):
    for book in books:
        print(book[0], "by:", book[1], "(Pub Date:", book[3], ")", "Genre:", book[4])


def show_menu():
    print("I Read in 1138 books")
    print("What would you like to do?")
    print("\t 1: Look up year range")
    print("\t 2: Look up month/year")
    print("\t 3: Search for author")
    print("\t 4: Search for title")
    print("\t Q: Quit")


def yearRange(books):
    years = [books[3]]
    start_year = int(input("Enter start year: "))
    end_year = int(input("Enter end year: "))
    # if start_year <= years <= end_year:
    showBooks(books)


def month_year(books):
    month = books[3]
    year = books[3]
    months = int(input("Enter month(1-12):"))
    years = int(input("Enter year:"))
    # If Statement:
    showBooks(books)


def search_author(books):
    author = books[2]
    authors = input("Enter search string:")
    # If Statement:
    showBooks(books)


def search_title(books):
    title = books[1]
    titles = input("Enter search string:")
    # If Statement:
    showBooks(books)


main()
