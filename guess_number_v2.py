# guess_number_v2.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def main():
    play_game()


def play_game():
    import random
    the_number = random.randint(1, 100)
    total_guesses = 0
    loop_continue = True
    while loop_continue:
        print("\nEnter your guess: (-1 to quit)")
        guess = int(input())
        if guess == -1:
            break
        diff = abs(the_number - guess)
        if diff == 0:
            message = "CORRECT"
        elif diff <= 5:
            message = "HOT"
        elif diff <= 10:
            message = "VERY WARM"
        elif diff <= 20:
            message = "WARM"
        elif diff <= 40:
            message = "LUKEWARM"
        else:
            message = "COLD"
        print(message)
        total_guesses += 1
        if total_guesses == 5:
            the_number = random.randint(1, 100)
            print("\nSorry, not quick enough. The secret number has moved.")

        elif total_guesses > 1 and diff != 0:
            if diff < diff_last:
                print('Getting warmer')
            if diff > diff_last:
                print('Getting colder')
        diff_last = diff
        if diff == 0:
            loop_continue = False
    print(f'\nYou made {total_guesses} guesses.')


main()
