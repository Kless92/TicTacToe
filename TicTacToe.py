from TicTacToeBorder import create_bord, check_turn, check_win
from TicTacToeAI import midMax
import os
setup = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
#class TicTacToeBord():


playing  = True
turn = 0 
prev_turn = -1
complete  = False
oneOrTwo = True

while True:
    print('Type "1" for Player vs AI or "2" for Players vs Player: ')
    a = input()
    if (a == '1'):
        aiPlayer = False
        break
    elif (a == '2'):
        aiPlayer = True
        break
    else:
        print('Not a valid input!')
        input()

while playing:
    #Below is Clear operator
    os.system('cls' if os.name== 'nt' else 'clear')
    create_bord(setup)

    if prev_turn == turn:
        print('Invalid spot selected!')
    prev_turn = turn
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
    #Check if P1 or P2 has won
    print('Near check win')
    if check_win(setup):
        playing, complete = False, True
    #Checks if P1 or P2 has Draw
    print('Near turn greater then 8')
    if turn > 8:
        playing = False
        break
    #If AI is Second player
    if aiPlayer is False and turn % 2 != 0:    
        turn += 1
        setup[midMax(setup)] = check_turn(turn)
        os.system('cls' if os.name== 'nt' else 'clear')
        create_bord(setup)
        input()
        #Check if the AI has won this game.
        print('Near check win')
        if check_win(setup):
         playing, complete = False, True


os.system('cls' if os.name== 'nt' else 'clear')
create_bord(setup)

if complete:
    if check_turn(turn) == 'X':
        print('Player 1 Wins!')
    else:
        print('Player 2 Wins!')
else:
    print('This game is a draw!')