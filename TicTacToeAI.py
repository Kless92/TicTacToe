import random
numX = 1
numO = 0
#update numX for new turns
def midMax(setup):
    if numX == 1:
        return oneX(setup)
    elif numX == 2:
        print('Place Holder')
    elif numX == 3:
        print('Place Holder')
    elif numX == 4:
        print('Place Holder')
    else:
        return

def oneX(setup):
    num = random.randint(1, 9)
    if (setup[num] == 'X'):
        return oneX(setup)
    else:
        return num
    