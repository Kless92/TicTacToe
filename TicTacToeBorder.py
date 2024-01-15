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