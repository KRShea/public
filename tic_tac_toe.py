"""
Course: Python for Scientists (Part-I)
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Kristopher Shea'
#%%
import random
##import copy
# %%

def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    for i in range(0,3):
        print(*Board[i], sep = "|")
        print('-+-+-' if i < 2 else '')
    pass
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        (1) return True  if Board[i][j] is empty (' ')
        (2) return False if Board[i][j] is not empty
        (3) return False if i or j is invalid (e.g. i = -1 or 100)
        think about the order of (1) (2) (3)
    '''
    
    if Board[i][j] == ' ':
        return True
    else: 
        return False
    
    pass
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in range(0,3)
              for j in range(0,3)
                  add one to the counter if Board[i][j] is not empty
    '''
    pieces = 0
    for i in range(0,3):
        for j in range(0,3):
            if Board[i][j] in ['X','O']:
                pieces += 1
    return pieces
    pass
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
 
    if  GetNumberOfChessPieces(Board) == 9:
        return True
    else:
        return False
    pass
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if  GetNumberOfChessPieces(Board) == 0:
        return True
    else:
        return False
    pass
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag at the location (row, col)
    '''
    Board[int(Choice[0])][int(Choice[1])] = Tag
    
    pass
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    valid_choice = {0,1,2}
    print("let's play ...................")
    print("Tic Tac Toe?")
    while True:
       
        #print("or you want to see a record of the game (g)?")
        #print("or you want to quit(q)?", end='')
        try: 
            user_row = int(input("please choose row:0,1,2"))
        except:
            print('Please use only numbers 0,1,2')
            continue
        try:     
            user_col = int(input("please choose column:0,1,2"))
        except:
            print('Please use only numbers 0,1,2')
            continue

        if (user_row in valid_choice) and (user_col in valid_choice):
            HumanChoice = (user_row,user_col)  
            print(f'row = {user_row}')
            print(f'col = {user_col}')
            if Board[HumanChoice[0]][HumanChoice[1]] != ' ':
                 print('Please Select a Vacant Spot')
                 continue            
            break
        else:
            print("The computer does not understand your input")
    return HumanChoice
    pass
#%%
def ComputerPlayer(Tag, Board):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if the spot is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
   
    boardCopy = [x[:] for x in Board]
    opposingTag = ('X' if Tag == 'O' else 'O')

    win = ('','')
    stopWin = ('','')

    bestMoves = [(1,1),(0,0),(0,2),(2,0),(2,2)]

    availableMoves = []
    for i in range(0,3):
        for j in range(0,3):
            if boardCopy[i][j] == ' ':
                availableMoves.append((i,j))
    
    for i in availableMoves:
        ##print(i)
        boardTmp = [x[:] for x in boardCopy]
        boardTmp[i[0]][i[1]] = Tag
        if Judge(boardTmp) == (1 if Tag == 'X' else 2):
            win = i
        boardTmp = [x[:] for x in boardCopy]
        boardTmp[i[0]][i[1]] = opposingTag
        if Judge(boardTmp) == (2 if Tag == 'X' else 1):
            stopWin = i

    if win != ('',''):
        return win
    elif stopWin != ('',''):
        return stopWin
    elif next(i for i in bestMoves if i in availableMoves) is not None:
        return next(i for i in bestMoves if i in availableMoves)
    else:
        return  availableMoves[random.randrange(0, len(availableMoves))]
    pass
#%%
def Judge(Board):
    '''
    Parameter:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
            use a if-statment to check if three 'X'/'O' in a row
        (2) if no one wins, then check if it is a tie
            note: if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress        
    '''
    
    boardTranspose = [[x[i] for x in Board] for i in range(len(Board[0]))]
    boardInv = Board[::-1]
    rows = ''
    columns = ''
    boardStr = ''
    diag1 = ''
    diag2 = ''
        #rows
    for i in range(0,3):
        rows += ''.join(Board[i]) + ('_' if i < 2 else '')
        #columns
    for i in range(0,3):
        columns += ''.join(boardTranspose[i]) + ('_' if i < 2 else '')
    #diagonal1
    for i in range(0,3):
        diag1 += str(Board[i][i])
    #diagonal2
    for i in range(0,3):
        diag2 += str(boardInv[i][i])
    boardStr = rows + '_' + columns + '_' + diag1 + '_' + diag2
    
    Outcome = 0
    if ' ' not in boardStr: 
        Outcome = 3
    if 'XXX' in boardStr:
        Outcome = 1
    if 'OOO' in boardStr:
        Outcome = 2

    return Outcome

        
#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    ''' 
    if Outcome == 0:
       print('the game is still in progress')
    if Outcome == 1:
        print(f'{NameX} is the Winner (X)')
    if Outcome == 2:
        print(f'{NameO} is the Winner (O)')
    if Outcome == 3:
       print('it is a tie')
    pass
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get a choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    
    
    while True:
                
        if NameX == 'ComputerPlayer':
            UpdateBoard(Board, 'X', ComputerPlayer('X', Board) )
        else:
            UpdateBoard(Board, 'X', HumanPlayer('X',Board) )
    
        for i in range(0,3):
            print('.........')
        print(f'{NameX} X has made selection')
        DrawBoard(Board)
       
        Outcome = Judge(Board)
        ShowOutcome(Judge(Board), NameX, NameO)
        if Outcome in {1,2,3}:
            break
    
        if NameO == 'ComputerPlayer':
            UpdateBoard(Board, 'O', ComputerPlayer('O', Board) )
        else:
            UpdateBoard(Board, 'O', HumanPlayer('O',Board) )
    
        for i in range(0,3):
            print('.........')
        print(f'{NameO} O has made selection')
        DrawBoard(Board)
    
        Outcome = Judge(Board)
        ShowOutcome(Outcome, NameX, NameO)
        if Outcome in {1,2,3}:
            break
    
    
    pass
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()












