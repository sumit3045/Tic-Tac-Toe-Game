# ------Global Variables_______
# Game board
board=["-" for elements in range(9)]

# If game is still going
game_still_going= True

# Who won? or Tie?
winner= None

# Who's turn is it?
current_player= "X"

# Display board
def display_board():

    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic-tac-toe
def play_game():

    # Displays board
    display_board()

    # while the game is still going
    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)


        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()


# The game has ended

    if winner=='X' or winner=='O':
        print(winner + ' won')
    elif winner== None:
        print("Tie")


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print("The current player:"+player)
    position=(input("Choose your position: "))

    valid=False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("INVALID INPUT! Choose your position from (1-9): ")

        position=int(position)-1
        if board[position] == '-':
            valid=True
        else:
            print("You cant go there!Go again")

    board[position]=player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable
    global  winner

    #If check_rows works, either X or O will be o/p. Otherwise all time o/p will be None
    row_winner=check_rows()


    #columns
    column_winner=check_columns()

    #diagonals
    diagonal_winner=check_diagonals()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner= None

    return
def check_rows():
    #set up global variable
    global  game_still_going
    # check if any the rows have the same value
    row_1 = board[0] == board[1] == board[2] !='-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    #If any of the rows does have a match flag that as a win

    if row_1 or row_2 or row_3:
        game_still_going= False
    #Return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    # set up global variable
    global game_still_going
    # check if any the colmns have the same value
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    # If any of the colmns does have a match flag that as a win

    if col_1 or col_2 or col_3:
        game_still_going = False
    # Return winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    return

def check_diagonals():
    # set up global variable
    global game_still_going
    # check if any the diagonals have the same value
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[2] == board[4] == board[6] != '-'


    # If any of the diags does have a match flag that as a win

    if diag_1 or diag_2:
        game_still_going = False
    # Return winner X or O
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going= False
    return

def flip_player():
    #global variables we need
    global current_player
    #if current player was X, change to O
    if current_player =='X':
        current_player ="O"
    # if current player was O, change to X
    elif current_player=="O":
        current_player='X'
    return

play_game()


