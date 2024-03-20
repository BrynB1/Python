autom = {}
autom[('s0', '0')] = 's1'
autom[('s0', '1')] = 's0'
autom[('s1', '0')] = 's2'
autom[('s1', '1')] = 's0'
autom[('s2', '0')] = 's2'
autom[('s2', '1')] = 's0'
accept = ['s2']


def go(start, intStr, autom, accept):
    currState = start
    for i in range(0, len(intStr)):
        tup = currState, intStr[i]
        currState = autom[tup]

    if currState in accept:
        return "yes"
    else:
        return "no"


print(go('s0', '000000', autom, accept))
print(go('s0', '0000110', autom, accept))