A_list = [' ' , ' ' , ' ']
B_list = [' ' , ' ' , ' ']
C_list = [' ' , ' ' , ' ']

win = False

def win_check():
        global A_list , B_list , C_list
        if A_list[0] == A_list[1]  == A_list[2] == 'X': #X X X
            print(' player 1 wins')
            return 'player1wins'
        elif A_list[0] == A_list[1] == A_list[2]  == 'O':#O O O
            print(' player 2 wins')
            return 'player2wins'
        elif A_list[0] == B_list[0]  == C_list[0]  == 'X':#X
            print(' player 1 wins')                     #X
            return 'player1wins'                        #X
        elif A_list[0] == B_list[0]  == C_list[0]  == 'O':#O
            print(' player 2 wins')                     #O
            return 'player2wins'                        #O
        elif A_list[0] == B_list[1]  == C_list[2]  == 'X':#X
            print(' player 1 wins')                     #  X
            return 'player1wins'                        #    X
        elif A_list[0] == B_list[1] == C_list[2]  == 'O':#O
            print(' player 2 wins')                    #  O
            return 'player2wins'                       #    O
        elif A_list[2] == B_list[1] == C_list[0]  == 'X':#    X
            print(' player 1 wins')                    #  X
            return 'player1wins'                       #X
        elif A_list[2]==B_list[1]== C_list[0]== 'O':#    O
            print(' player 2 wins')               #  O
            return 'player2wins'                  #O  
        elif C_list[0] == C_list[1]  == C_list[2]  == 'X':
            print(' player 1 wins')
            return 'player 1 wins'                   #X X X
        elif C_list[0] == C_list[1] == C_list[2]  == 'O':
            print(' player 2 wins')
            return 'player 2 wins'                   #O O O
        elif A_list[2] == B_list[2] == C_list[2] == 'X':#    X
            print(' player 1 wins')                #       X
            return 'player1wins'                  #        X
        elif A_list[2] == B_list[2] == C_list[2] == 'O':#    O
            print(' player 2 wins')                   #    O
            return 'player2wins'                      #    O
        elif A_list[1] == B_list[1]  == C_list[1]  == 'X':#X
            print(' player 1 wins')                     #X
            return 'player1wins'                        #X
        elif A_list[1] == B_list[1] == C_list[1]  == 'O':# O
            print(' player 2 wins')                    # O
            return 'player2wins'                       # O
        elif B_list[0] == B_list[1]  == B_list[2]  == 'X':#
            print(' player 1 wins')                     # X X X
            return 'player1wins'                        #
        elif B_list[0] == B_list[1]  == B_list[2]  == 'O':#
            print(' player 2 wins')                     # O O O
            return 'player2wins'
        else:
              return False
        
def move_player_1():
    move = input('Enter move for player 1 such as A1/C3: ')

    if move == 'A1'  and A_list[0] == " ":
            
                A_list[0] = "X"
    elif move == 'A2'  and A_list[1] == " ":
        
            A_list[1] = "X"
    elif move == 'A3'  and A_list[2] == " ":
        
            A_list[2] = "X"
    elif move == 'B1'  and B_list[0] == " ":
        
            B_list[0] = "X"
    elif move == 'B2'  and B_list[1] == " ":
        
            B_list[1] = "X"
    elif move == 'B3'  and B_list[2] == " ":
        
            B_list[2] = "X"
    elif move == 'C1'  and C_list[0] == " ":
        
            C_list[0] = "X"
    elif move == 'C2'  and C_list[1] == " ":
        
            C_list[1] = "X"
    elif move == 'C3'  and C_list[2] == " ":
        
            C_list[2] = "X"
    else:
        print("Invalid move Try Again! :P")
        return move_player_1()

def move_player_2():
        move = input('Enter move for player 2 such as A1/C3: ')
        if move == 'A1'  and A_list[0] == " ":
            
                A_list[0] = "O"
        elif move == 'A2'  and A_list[1] == " ":
            
                A_list[1] = "O"
        elif move == 'A3'  and A_list[2] == " ":
            
                A_list[2] = "O"
        elif move == 'B1'  and B_list[0] == " ":
            
                B_list[0] = "O"
        elif move == 'B2'  and B_list[1] == " ":
            
                B_list[1] = "O"
        elif move == 'B3'  and B_list[2] == " ":
            
                B_list[2] = "O"
        elif move == 'C1'  and C_list[0] == " ":
            
                C_list[0] = "O"
        elif move == 'C2'  and C_list[1] == " ":
            
                C_list[1] = "O"
        elif move == 'C3'  and C_list[2] == " ":
            
                C_list[2] = "O"
        else:
              print("Invalid move Try Again! :P")
              move_player_2()

player1_move = True
player2_move = False

while win != True:
    
    print("      1         2            3")
    print("A:   " , A_list[0] ,"  |   " , A_list[1] ,  "   |     " ,   A_list[2])
    print("  ---------------------------")
    print("B:   " , B_list[0] ,"  |   " , B_list[1]  , "   |     " ,   B_list[2])
    print("  ---------------------------"  )
    print("C:   " , C_list[0] ,"  |   " , C_list[1]   ,"   |     " ,   C_list[2])

    if player1_move:
          move_player_1()
          player1_move = False
          player2_move = True
          if win_check() != False:
                print(win_check())
                break
    
    print("      1         2            3")
    print("A:   " , A_list[0] ,"  |   " , A_list[1] ,  "   |     " ,   A_list[2])
    print("  ---------------------------")
    print("B:   " , B_list[0] ,"  |   " , B_list[1]  , "   |     " ,   B_list[2])
    print("  ---------------------------"  )
    print("C:   " , C_list[0] ,"  |   " , C_list[1]   ,"   |     " ,   C_list[2])


    if player2_move:
          move_player_2()
          player2_move = False
          player1_move = True
          if win_check() != False:
                print(win_check())
                break
    
leave = ''
while leave == '':
        leave = input('Enter any character to leave program: ')