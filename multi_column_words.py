# multi_column_words.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def main():
    file = open('eldrow_words.txt', 'r')
    column_out(10, file)
    file.close()


def column_out(columns, wordlist_file):
    counter = 0
    words = ""
    for line in wordlist_file.readlines()[4:]:
        line = line.strip()
        words += line + " "
        counter += 1
        if counter == 10:
            words += "\n"
            counter = 0
    print(words)


# Call the main function.
if __name__ == '__main__':
    main()
