
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

# bo : board
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):  
            # length of each row
            if bo[i][j] == 0:
                return (i, j)  # row , column

    return None

#Solves a sudoku board using backtracking  ,  bo: 2d list of ints
def solve(bo): 
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

# Returns if the attempted move is valid  ,  param pos: (row, col)
def valid(bo, pos, num):  

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

print_board(board)
solve(board)
print("____________________________")
print()
print_board(board)