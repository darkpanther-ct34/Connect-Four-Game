def check(board,piece):
    #check all horizonal
    ROW_COUNT = 6
    COL_COUNT = 7
    for col in range(COL_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    #check for vertical
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    # check diagonal posative
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    # check for negative diagonal
    for row in range(3,ROW_COUNT):
        for col in range(COL_COUNT-3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
