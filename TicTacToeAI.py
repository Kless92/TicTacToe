import random

combList= [[2, 3, 4, 5, 6],
           [1, 3, 5, 8],
           [1, 2, 5, 6, 7, 9],
           [1, 5, 6, 7],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [3, 4, 5, 9],
           [1, 3, 4, 5, 8, 9],
           [2, 5, 7, 9],
           [1, 3, 5, 6, 7, 8]]
#update numX for new turns
def midMax(setup):
    numX = []
    numO = []
    a = list(setup.keys())
    for x in setup:
        #All all dect value that has X to numX
        if setup[x] == 'X':
            numX.append(a[x-1])
            print(numX)
        #All all dect value that has O to numO
        elif setup[x] == 'O':
            numO.append(a[x-1])
            print(numO)
    if len(numX) == 1:
        return oneX(setup)
    else:
        return findXTwins(setup, numX, numO)

def oneX(setup):
    num = random.randint(1, 9)
    if (setup[5] != 'X' or setup[5] != 'O'):
        return 5
    elif (setup[num] == 'X'):
        return oneX(setup)
    else:
        return num

def findXTwins(setup, xList, oList):
    print(len(xList))
    print(len(oList))
    input()
    for x in range(10):
        print(x)
        if x in xList:
            print(combList[x-1])
            test = len(combList[x-1])
            print('aaa')
            input()
            for y in (combList[x-1]):
                print(y)
                print('bbb')
            input()    
        else:
            print(False)
    input()

    #if (setup[1] == 'X' and setup[2] == 'X'):
        #return 3
    #elif(setup[1] == 'X' and setup[3] == 'X'):
       # return 2
    #elif(setup[2] == 'X' and setup[3] == 'X'):
        #return 1

    