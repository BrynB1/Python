# CS175L-01
# Bryn Bijur
# restaurant

# Define
vegetarian = False
vegan = False
gluten_free = False
restart = True
print("Please type (yes) or (no) for all questions.")
# Input
while restart:
    response = input("Is anyone in your party a vegetarian?: ")
    if response == 'yes':
        vegetarian = True
    else:
        vegetarian = False
    response = input("Is anyone in your party a vegan?: ")
    if response == 'yes':
        vegan = True
    else:
        vegan = False
    response = input("Is anyone in your party gluten-free?: ")
    if response == 'yes':
        gluten_free = True
    else:
        gluten_free = False
    # Output
    print("Here are your restaurant choices:")
    if vegetarian == False and vegan == False and gluten_free == False:
        print("Joe's Gourmet Butgers")
        print("Corner Cafe")
        print("The Chef's Kitchen")
        print("Mama's Fine Italian")
        print("Main Street Pizza")
    elif vegan == False and gluten_free == False:
        print("Mama's Fine Italian")
        print("Corner Cafe")
        print("The Chef's Kitchen")
    elif not vegan:
        print("Main Street Pizza")
        print("Corner Cafe")
        print("The Chef's Kitchen")
    else:
        print("Corner Cafe")
        print('The Chef\'s Kitchen')
    response = input("Would you like to do another restaurant search?: ")
    if response == 'yes':
        restart = True
    if response == 'no':
        restart = False
