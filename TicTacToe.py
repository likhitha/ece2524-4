X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    print \
            """
            You will make your move known by entering a number, 0 - 8. 
	    The number will correspond to the board position as illustrated:

                                         0 | 1 | 2
                                        -----------
                                         3 | 4 | 5
                                        -----------
                                         6 | 7 | 8

            """
# ask for response 
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response
# ask for number response    
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response
# ask whether ready to start        
def pieces():
    go_first = ask_yes_no("Are you ready to start? (press y to start): ")
    if go_first == "y":
        print "\nTake the first move"
        human = X
        computer = O
    return computer, human
# make new board    
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
# display board    
def display_board(board):
    print "\n\t", board[0], "|", board[1], "|", board[2]
    print "\t", "---------"
    print "\t", board[3], "|", board[4], "|", board[5]
    print "\t", "---------"
    print "\t", board[6], "|", board[7], "|", board[8], "\n"
# check for legal move    
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves    
# 8 different combinations to win    
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
            
        if EMPTY not in board:
            return TIE            
        return None
# player's turn    
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Select your move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print "\nThat square is already occupied.\n"
    return move
# computer's turn    
def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print move
            return move
        board[move] = EMPTY
        
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print move
            return move
        board[move] = EMPTY
        
    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print move
            return move
            
def next_turn(turn):
    if turn == X:
        return 0
    else:
        return X
# print the winner        
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print the_winner, "won!\n"
    else:
        print "Tie!\n"
   
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
        
main()
