# prob1.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
# Create the list called prob1_reverse
prob1_list1 = [90, 29, 26, 33, 63, 91, 77, 68, 31, 77, 84, 95, 27, 68, 55, 28, 60, 27, 21, 25, 85, 53, 5, 25, 87, 63,
               52, 40, 20, 13, 20, 37, 44, 44, 20, 17, 80, 96, 72, 74, 39, 13, 87, 66, 80, 1, 35, 40, 40, 47, 7, 60, 56,
               30, 29, 70, 69, 40, 38, 17, 43, 69, 11, 46, 93, 6, 92, 14, 36, 70, 98, 80, 6, 27, 44, 6, 41, 70, 34, 78,
               81, 93, 95, 49, 78, 84, 12, 20, 44, 7, 19, 60, 91, 43, 94, 57, 17, 49, 48]
prob1_reverse = []
prob1_list1.reverse()
for n in prob1_list1:
    prob1_reverse.append(n)
print(prob1_reverse)
# revert code
prob1_list1.reverse()
# Create the list called prob1_sorted
prob1_sorted = []
prob1_list1.sort()
for n in prob1_list1:
    prob1_sorted.append(n)
print(prob1_sorted)
# Create the list called prob1_duplicated
prob1_dupe = []
for e in prob1_list1:
    counter = 0
    for x in prob1_list1:
        if e == x:
            counter += 1
    if counter > 1:
        prob1_dupe.append(e)
prob1_dupe = sorted(prob1_dupe)
prob1_duplicated = []
for i in prob1_dupe:
    if i not in prob1_duplicated:
        prob1_duplicated.append(i)
print(prob1_duplicated)


