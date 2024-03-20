# guess_number.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
import random

correct = random.randint(1, 100)
repeat = True
guess = 0
dif = 0
dif2 = 0
fill = ""
tries = 0
while repeat:
    tries += 1
    guess = int(input("Guess a number from 1 to 100:(-1 to quit):"))
    dif = correct - guess
    dif2 = abs(dif)
    if guess == -1:
        break
    if dif2 == 0:
        fill = "Correct"
        repeat = False
    elif dif2 <= 5:
        fill = "Hot"
    elif dif2 <= 10:
        fill = "Very Warm"
    elif dif2 <= 20:
        fill = "Warm"
    elif dif2 <= 40:
        fill = "LUKEWARM"
    else:
        fill = "Cold"
    print(fill)
    print("Number of tries:", tries)
