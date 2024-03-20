# prob2.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022

def compare_lists(x, y):
    if len(x) != len(y):
        return False
    for index in range(0, len(x)):
        if x[index] != y[index]:
            return False
    return True


# Test
print(compare_lists([1, 2, 3], [1, 2, 3]))
print(compare_lists([1, 2], [1, 2, 3]))
print(compare_lists([3, 1, 2], [1, 2, 3]))
print(compare_lists(['fee', 'fo', 'fi'], ['fee', 'fo', 'fi']))
print(compare_lists(['fee', 'fo', 'fi', 'fum'], ['fee', 'fo', 'fi']))
