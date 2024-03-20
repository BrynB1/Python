# prob3.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def str_mask(x, y):
    if len(x) != len(y):
        return "Error unequal length"
    test = ""
    for index in range(0, len(x)):
        if x[index] != y[index]:
            test += "X"
        else:
            test += x[index]
    return test


# Test
print(str_mask('abC', 'abC'))
print(str_mask('aEv', 'AeV'))
print(str_mask('Pwn3d', 'owned'))
print(str_mask('Rebus Dunderdorf', 'ReBus Dumblebum'))
