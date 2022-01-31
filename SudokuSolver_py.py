sudokuBoard = [[0,0,3,0,9,0,4,0,1],
               [1,9,4,0,7,2,0,0,8],
               [0,0,8,4,0,0,0,0,0],
               [9,0,0,0,0,0,0,0,2],
               [0,8,1,0,3,5,0,0,0],
               [2,6,7,0,8,4,1,5,0],
               [0,1,0,0,0,0,7,8,5],
               [8,5,6,7,0,0,9,0,0],
               [7,0,0,0,0,8,0,1,0]]

GRID_SIZE = 9

def isInRow(board, row, number):
    for i in range(GRID_SIZE):
        if board[row][i] == number:
            return True
    return False

def isInColumn(board, column, number):
    for i in range(GRID_SIZE):
        if board[i][column] == number:
            return True
    return False

def isInBox(board, row, column, number):
    row -= row % 3
    column -= column % 3
    for i in range(3):
        for j in range(3):
            if board[row + i][column + j] == number:
                return True
    return False

def isValidPlacement(board, row, column, number):
    if not isInRow(board, row, number) and \
            not isInColumn(board, column, number) and \
            not isInBox(board, row, column, number):
        return True
    return False

def solveSudoku(board):
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            aNumber = board[row][column]
            if aNumber == 0:
                for number in range(1, GRID_SIZE+1):
                    if isValidPlacement(board, row, column, number):
                        board[row][column] = number
                        if solveSudoku(board):
                            return True
                        else:
                            board[row][column] = 0
                return False
    return True

i = 0
for row in sudokuBoard:
    j = 0
    if i % 3 == 0 and i != 0:
        print("---------------------")
    for column in row:
        if j % 3 == 0 and j != 0:
            print("|", end=" ")
        print(column, end=" ")
        j += 1
    print()
    i += 1
print()
if solveSudoku(sudokuBoard):
    print("Solved succesfully!")
    i = 0
    for row in sudokuBoard:
        j = 0
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for column in row:
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(column, end=" ")
            j += 1
        print()
        i += 1
else:
    print("#Unsolvable :(")


