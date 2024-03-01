import random
numX = 0
numO = 0
#update numX for new turns
def midMax(setup, num):
    numX = num - 1
    if numX == 1:
        return oneX(setup)
    #elif numX == 2:
       # return twoX(setup)
    #elif numX == 3:
       # print('Place Holder')
    #elif numX == 4:
       # print('Place Holder')
    else:
        return twoX(setup)

def oneX(setup):
    num = random.randint(1, 9)
    if (setup[num] == 'X'):
        return oneX(setup)
    else:
        return num

def twoX(setup):
    if (setup[1] == 'X' and setup[2] == 'X'):
        return 3
    else:
        return 0
    