# multi_column_words.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def main():
    infile = open('cs176roster.webadvisor.txt', 'r')
    generate_roster(infile)


def generate_roster(student_records_file):
    counter = 0
    students = ""
    for line in student_records_file.readlines():
        counter += 1
        line = line.strip()
        if counter == 1:
            students += line + ", "
        elif counter == 4:
            students += line + ", "
        elif counter == 5:
            students += line + ", "
        elif counter == 6:
            students += line
        elif counter == 8:
            counter = 0
            students += "\n"
    outfile = open("roster.txt", 'w')
    outfile.write(students)


main()
