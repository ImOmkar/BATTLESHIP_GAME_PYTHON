#START

from random import randint
import time


#Board = [[],[],[],[],[]]
Board = []
Board_size = 5

for i in range(0, 5):
    Board.append(['O'] *5)

def Print_Board(Board):
    for i in Board:
        print(" ".join(i))
    #Board[i]=['0']*5
        
Print_Board(Board)

def random_row(Board):
    return randint(0, len(Board) - 1)

def random_col(Board):
    return randint(0, len(Board[0]) - 1)
        
ship_row = random_row(Board)
ship_col = random_col(Board)

print('=========================')

print('=========================')

for turn in range(4):
    print('Turn', turn + 1)
    
    guess_row = int(input('Guess Row: '))
    guess_col = int(input('Guess Col: '))

    print('==================================================')

    print('Breathe in... Breathe out...')

    print('==================================================')

    
    time.sleep(4)#will take time to show the result(Excitement purpose)
    
    if guess_row == ship_row and guess_col == ship_col:
        print('WINNER WINNER CHICKEN DINNER!! You Sank My Battleship!')
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print('Oops, Thats not even in the ocean')
        
        elif Board[guess_row][guess_col]=='X':
            print('You missed that one already!!')
            
        else:
            print('Sorry! You missed my battleship!!')
            Board[guess_row][guess_col]='X'
            #Print_Board(Board)
            if turn == 3:
                print('Game Over')
        #print (turn +1) here!
        Print_Board(Board)

print('==================================================')

print('SHIP WAS AT',ship_row,'ROW','AND',ship_col,'COLUMN')#for checking purpose

#END


   




