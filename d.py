# d.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022

#   DDDD
#   D   D
#   D   D
#   D   D
#   DDDD
#
def d(symbol, line):
    s = symbol
    line1 = s * 4
    line2 = f'{s}   {s} '
    line3 = f'{s}   {s} '
    line4 = f'{s}   {s} '
    line5 = line1
    if line == 1:
        return line1
    elif line == 2:
        return line2
    elif line == 3:
        return line3
    elif line == 4:
        return line4
    elif line == 5:
        return line5
    return "Invalid line"


def main():
    # test function d()
    print(d('%', 1))
    print(d('4', int('4')))

if __name__ == '__main__':
    main()
