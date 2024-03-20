# CS175L-01
# Bryn Bijur
# mostFrequent.py


string = str(input("Enter a string: "))
letters = {}
for i in string:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
frequent = max(letters)
print("The character that appears most frequently in the string is : ", str(frequent))
