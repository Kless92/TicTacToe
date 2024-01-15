def create_bord(input):
    num = 3
    for i in range(3):
        print(f'{input[num-2]}|{input[num-1]}|{input[num]}')
        if i < 2:
            print('-|-|-')
            num = num + 3
    #print(f'{input[1]}|{input[2]}|{input[3]}')
    #print('-|-|-')
    #print(f'{input[4]}|{input[5]}|{input[6]}')
    #print('-|-|-')  
    #print(f'{input[7]}|{input[8]}|{input[9]}')
            
#This function will keep the players turns of P1 and P2
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
    
def check_win(input):
    if (input[1] == 'X' and input[2] == 'X' and input[3] == 'X' or input[1] == 'O' and input[2] == 'O' and input[3] == 'O') \
     or (input[4] == 'X' and input[5] == 'X' and input[6] == 'X' or input[4] == 'O' and input[5] == 'O' and input[6] == 'O')  \
     or (input[7] == 'X' and input[8] == 'X' and input[9] == 'X' or input[7] == 'O' and input[8] == 'O' and input[9] == 'O') :
        print('Row')
        return True
    elif  (input[1] == 'X' and input[4] == 'X' and input[7] == 'X' or input[1] == 'O' and input[4] == 'O' and input[7] == 'O') \
     or (input[2] == 'X' and input[5] == 'X' and input[8] == 'X' or input[2] == 'O' and input[5] == 'O' and input[8] == 'O')  \
     or (input[3] == 'X' and input[6] == 'X' and input[9] == 'X' or input[3] == 'O' and input[6] == 'O' and input[9] == 'O') :
        print('Col')
        return True
    elif  (input[1] == 'X' and input[5] == 'X' and input[9] == 'X' or input[1] == 'O' and input[5] == 'O' and input[9] == 'O') \
     or (input[3] == 'X' and input[5] == 'X' and input[7] == 'X' or input[3] == 'O' and input[5] == 'O' and input[7] == 'O'):
        print('Diangle')
        return True
    else:
        return False