
A_list = [ " " , " " , " "]
B_list = [ " " , " " , " "]
C_list = [ " " , " " , " "]
list = [A_list , B_list , C_list]
move1 = ""
move2 = ""
play = True
play1 = True
play2 = False
print("      1         2            3")
print("A:   " , A_list[0] ,"  |   " , A_list[1] ,  "   |     " ,   A_list[2])
print("  ---------------------------")
print("B:   " , B_list[0] ,"  |   " , B_list[1]  , "   |     " ,   B_list[2])
print("  ---------------------------"  )
print("C:   " , C_list[0] ,"  |   " , C_list[1]   ,"   |     " ,   C_list[2])

while play == True:
        
    

    def win( play ):
        if A_list[0] == A_list[1]  == A_list[2] == 'X': #X X X
            print(' player 1 wins')
            return 'player1wins'
        if A_list[0] == A_list[1] == A_list[2]  == 'O':#O O O
            print(' player 2 wins')
            return 'player2wins'
        if A_list[0] == B_list[0]  == C_list[0]  == 'X':#X
            print(' player 1 wins')                     #X
            return 'player1wins'                        #X
        if A_list[0] == B_list[0]  == C_list[0]  == 'O':#O
            print(' player 2 wins')                     #O
            return 'player2wins'                        #O
        if A_list[0] == B_list[1]  == C_list[2]  == 'X':#X
            print(' player 1 wins')                     #  X
            return 'player1wins'                        #    X
        if A_list[0] == B_list[1] == C_list[2]  == 'O':#O
            print(' player 2 wins')                    #  O
            return 'player2wins'                       #    O
        if A_list[2] == B_list[1] == C_list[0]  == 'X':#    X
            print(' player 1 wins')                    #  X
            return 'player1wins'                       #X
        if A_list[2]==B_list[1]== C_list[0]== 'O':#    O
            print(' player 2 wins')               #  O
            return 'player2wins'                  #O  
        if C_list[0] == C_list[1]  == C_list[2]  == 'X':
            print(' player 1 wins')
            return 'player 1 wins'                   #X X X
        if C_list[0] == C_list[1] == C_list[2]  == 'O':
            print(' player 2 wins')
            return 'player 2 wins'                   #O O O
        if A_list[2] == B_list[2] == C_list[2] == 'X':#    X
            print(' player 1 wins')                #       X
            return 'player1wins'                  #        X
        if A_list[2] == B_list[2] == C_list[2] == 'O':#    O
            print(' player 2 wins')                   #    O
            return 'player2wins'                      #    O
        if A_list[1] == B_list[1]  == C_list[1]  == 'X':#X
            print(' player 1 wins')                     #X
            return 'player1wins'                        #X
        if A_list[1] == B_list[1] == C_list[1]  == 'O':# O
            print(' player 2 wins')                    # O
            return 'player2wins'                       # O
        if B_list[0] == B_list[1]  == B_list[2]  == 'X':#
            print(' player 1 wins')                     # X X X
            return 'player1wins'                        #
        if B_list[0] == B_list[1]  == B_list[2]  == 'O':#
            print(' player 2 wins')                     # O O O
            return 'player2wins'
    
    def replay():
        if win(play) == 'player1wins' or win(play) == 'player2wins':
            replay = str(input("Would you like to play again Y/N : "))
            replay = replay.upper()
            if replay == 'Y':
                A_list = [ " " , " " , " "]
                B_list = [ " " , " " , " "]
                C_list = [ " " , " " , " "]
            if replay == 'N':
                play == False
    def functionPlace1(move):

       
            
        if move == 'A1'  and A_list[0] == " ":
            
                A_list[0] = "X"
        if move == 'A2'  and A_list[1] == " ":
            
                A_list[1] = "X"
        if move == 'A3'  and A_list[2] == " ":
            
                A_list[2] = "X"
        if move == 'B1'  and B_list[0] == " ":
            
                B_list[0] = "X"
        if move == 'B2'  and B_list[1] == " ":
            
                B_list[1] = "X"
        if move == 'B3'  and B_list[2] == " ":
            
                B_list[2] = "X"
        if move == 'C1'  and C_list[0] == " ":
            
                C_list[0] = "X"
        if move == 'C2'  and C_list[1] == " ":
            
                C_list[1] = "X"
        if move == 'C3'  and C_list[2] == " ":
            
                C_list[2] = "X"
            
    if play1 == True:
        
        move1 = str(input("Where would player 1 like to move (specify in block pattern such as A1 or B3): " ))
        move1 = move1.upper()
        functionPlace1(move1)
        play1 = False
        play2 = True
       
    
    
    

    
    def functionPlace2(move):
        global play1
        global play2
        

            
        if move == 'A1'  and A_list[0] == " ":
            
                A_list[0] = "O"
        if move == 'A2'  and A_list[1] == " ":
            
                A_list[1] = "O"
        if move == 'A3'  and A_list[2] == " ":
            
                A_list[2] = "O"
        if move == 'B1'  and B_list[0] == " ":
            
                B_list[0] = "O"
        if move == 'B2'  and B_list[1] == " ":
            
                B_list[1] = "O"
        if move == 'B3'  and B_list[2] == " ":
            
                B_list[2] = "O"
        if move == 'C1'  and C_list[0] == " ":
            
                C_list[0] = "O"
        if move == 'C2'  and C_list[1] == " ":
            
                C_list[1] = "O"
        if move == 'C3'  and C_list[2] == " ":
            
                C_list[2] = "O"
    
    print("      1         2            3")
    print("A:   " , A_list[0] ,"  |   " , A_list[1] ,  "   |     " ,   A_list[2])
    print("  ---------------------------")
    print("B:   " , B_list[0] ,"  |   " , B_list[1]  , "   |     " ,   B_list[2])
    print("  ---------------------------"  )
    print("C:   " , C_list[0] ,"  |   " , C_list[1]   ,"   |     " ,   C_list[2])

    if win(play) ==  'player2wins':
        replay()
    if win(play) ==  'player1wins':
        replay()

    print(play)
    if play2 == True:
        
        move2 = str(input("Where would player 2 like to move (specify in block pattern such as A1 or B3): " ))
        move2 = move2.upeer()
        functionPlace2(move2)
        play2 = False
        play1 = True
        
        
    


    print("      1         2            3")
    print("A:   " , A_list[0] ,"  |   " , A_list[1] ,  "   |     " ,   A_list[2])
    print("  ---------------------------")
    print("B:   " , B_list[0] ,"  |   " , B_list[1]  , "   |     " ,   B_list[2])
    print("  ---------------------------"  )
    print("C:   " , C_list[0] ,"  |   " , C_list[1]   ,"   |     " ,   C_list[2])

    if win(play) ==  'player2wins':
        replay()
    if win(play) ==  'player1wins':
        replay() 
    


