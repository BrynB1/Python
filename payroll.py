payroll_file = open('payroll.dat', 'r')
linenum = 1
for line in payroll_file:
    if linenum ==  1:
        firstname = line
    elif linenum == 2:
        lastname = line
    elif linenum == 3:
        payrate = line
    elif linenum == 4:
        hours_worked = line
    else:
        linenum = 1
    linenum += 1
    print(firstname, lastname, payrate, hours_worked)
payroll_file.close()