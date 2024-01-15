from TicTacToeBorder import create_bord, check_turn
import os
setup = {1 : '·', 2 : '·', 3 : '·', 4 : '·', 5 : '·', 6 : '·', 7 : '·', 8 : '·', 9 : '·'}
#class TicTacToeBord():


playing  = True
turn = 0 

while playing:
    #Below is Clear operator
    os.system('cls' if os.name== 'nt' else 'clear')
    create_bord(setup)
    print("Player "+ str((turn % 2) + 1) + "'s turn:\nPick your spot or press q to quite!")
    choice = input()
    if choice == 'q':
        playing = False
    #Checks to see if player into is 1-9
    elif str.isdigit(choice) and int(choice) in setup:
        #Check if any of the spots are taken
        if not setup[int(choice)] in {'X', 'O'}:
            turn += 1
            setup[int(choice)] = check_turn(turn)