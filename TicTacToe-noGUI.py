board = {'A1' : ' ' , 'A2' : ' ' , 'A3' : ' ',
        'B1' : ' ' , 'B2' : ' ' , 'B3' : ' ',
        'C1' : ' ' , 'C2' : ' ' , 'C3' : ' '}
win = False

def win_check(board:dict):
       rows = ['A', 'B' , 'C']
       columns = ['1' , '2' , '3']

       for row in rows: #Horizontal Check
            position_1 , position_2 , position_3 = row + '1' , row + '2' , row + '3'
            print(position_1 , position_2 , position_2) 
            if board[position_1] == board[position_2] == board[position_3] and board[position_1] != ' ':
                   return board[position_1] , " wins"
        
       for column in columns: #Horizontal Check
            position_1 , position_2 , position_3 = 'A' + column , 'B' + column , 'C' + column
            if board[position_1] == board[position_2] == board[position_3] and board[position_1] != ' ':
                   return board[position_1] , " wins"
            
       #Diagonal Check
       if board['A1'] == board['B2'] == board['C3'] and board['A1'] != ' ':
             return board['A1'] + " wins"
       elif board['A3'] == board['B2'] == board['C1'] and board['A3'] != ' ':
             return board['A3'] + " wins"
                   
                    
        
        
def update_board(board:dict , player:str) -> None:
    player_convert = {'X' : 'player 1' , 'O' : 'player 2'}
    statement = f"Enter move for {player_convert[player]} such as A1/C3: "
    move = input(statement)



    if move not in board:
           print('Invalid Move , try again!')
           update_board(board , player)
    else:
        if board[move] != ' ':
               print('Invalid Move , try again!')
               update_board(board , player)
        else:
            board[move] = player

player1_move = True
player2_move = False

while True:
    
    print("      1         2            3")
    print("A:   " , board['A1'] ,"  |   " , board['A2'] ,  "   |     " ,   board['A3'])
    print("  ---------------------------")
    print("B:   " , board['B1'] ,"  |   " , board['B2']  , "   |     " ,   board['B3'])
    print("  ---------------------------"  )
    print("C:   " , board['C1'] ,"  |   " , board['C2']   ,"   |     " ,   board['C3'])

    if player1_move:
          update_board(board , 'X')
          player1_move = False
          player2_move = True

    print(win_check(board))
    if win_check(board )!= None:
          break
    print("      1         2            3")
    print("A:   " , board['A1'] ,"  |   " , board['A2'] ,  "   |     " ,   board['A3'])
    print("  ---------------------------")
    print("B:   " , board['B1'] ,"  |   " , board['B2']  , "   |     " ,   board['B3'])
    print("  ---------------------------"  )
    print("C:   " , board['C1'] ,"  |   " , board['C2']   ,"   |     " ,   board['C3'])

    if player2_move:
          update_board(board , 'O')
          player2_move = False
          player1_move = True
    
    print(win_check(board))
    if win_check(board )!= None:
          break