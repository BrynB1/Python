def main():
    import random
    m8 = open('m8_answers.txt', 'r')
    # (print all answers)
    # m8_answers = m8.read()
    # print(m8_answers)

    # Prints the first line
    m8_first = m8.readline()
    # Remove strip between answers
    print(m8_first.rstrip())
    # Prints the second line
    m8_second = m8.readline()
    print(m8_second)
    # ...


if __name__ == '__main__':
    main()
