import random

#update numX for new turns
def midMax(setup):
    numX = []
    a = list(setup.keys())
    for x in setup:
        if setup[x] == 'X':
            numX.append(a[x-1])
            print(numX)
    if len(numX) == 1:
        return oneX(setup)
    else:
        return findTwoXs(setup)

def oneX(setup):
    num = random.randint(1, 9)
    if (setup[num] == 'X'):
        return oneX(setup)
    else:
        return num

def findTwoXs(setup):
    if (setup[1] == 'X' and setup[2] == 'X'):
        return 3
    elif(setup[1] == 'X' and setup[3] == 'X'):
        return 2
    elif(setup[2] == 'X' and setup[3] == 'X'):
        return 1
    