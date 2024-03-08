import random

combList= [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [1, 4, 7],
              [1, 5, 9],
              [2, 5, 8],
              [3, 6, 9],
              [3, 5, 7]]
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
        return findXWins(setup, numX, numO)

def oneX(setup):
    num = random.randint(1, 9)
    #if the cent of the bord is empty, the AI will take it
    if (setup[5] != 'X' and setup[5] != 'O'):
        return 5
    #If any of the spots is taken it will call itself
    elif (setup[num] == 'X' or setup[num] == 'O'):
        return oneX(setup)
    else:
        return num

def findXWins(setup, xList, oList):
    print('xlist: ')
    print(len(xList))
    print('olist: ')
    print(len(oList))
    input()
    for x in combList:
        xFound = 0
        for y in x:
            if y in xList:
                print(True)
                xFound += 1
                if xFound == 2:
                    for z in x:
                        #print(z)
                        #input()
                        if setup[z] != 'X' and setup[z] != 'O':
                            return z
                    #input()
            else:
                print(False)
    #If the AI player 'can't' find a spot X could win; it will then all oneX()
    return oneX(setup)
    #input()

    