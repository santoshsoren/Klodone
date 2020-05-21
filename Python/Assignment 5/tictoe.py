
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

play = True
winner = None
player = "X" 
def display():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def game():
    display()
    while play:
        turn(player)
        check_game()
        flip_player()
    if winner =="X" or winner =="O":
        print(winner," won..!!")
    elif winner ==None:
        print("Game tie..!!")

def turn(player):
    print(player, "'s turn" )
    pos = int(input("Choose position: "))
    valid = False
    while not valid:
        while pos not in[1,2,3,4,5,6,7,8,9]:
            pos = int(input("Enter position between 1-9: "))
        pos -= 1
        if board[pos] == "-":
            valid = True
        else:
            print("This is invalid position. Please enter valid position.....!!!!! ")
    board[pos] = player    
    display()

def check_game():
    check_winner()
    tie()
    
def check_winner():
    global winner
    row_winner = row()
    column_winner = column()
    diagonal_winner = diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def row():
    global play
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        play = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

def column():
    global play
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        play = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None

def diagonal():
    global play
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        play = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None

def tie():
    global play
    if "-" not in board:
        play = False
        return True
    else:
        return False

def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

game()
