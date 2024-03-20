# display_letters.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022

from d import *

for row in range(1, 6):
    print(d('?', row), ' ', end='')
    print(d('!', row), ' ', end='')
    print(d('X', row))
