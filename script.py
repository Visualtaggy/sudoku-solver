board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def backtrackSolve(bo):
    find =  find_unsolved(bo)
    if not find:
        return True
    else:
        row, column = find
    
    for i in range (1,10):
        if check_validity(bo,i,(row,column)):
            bo[row][column] = i

            if backtrackSolve(bo):
                return True

            bo[row][column] = 0
    
    return False




def check_validity(bo,number,position):
    
    #Checking the row
    for i in range (len(bo[0])):
        if bo[position[0]][i] == number and  position[1] != i:
            return False
    #Checking the column
    for i in range (len(bo)):
        if bo[i] [position[1]] == number and position [0] != i:
            return False
    
    # checking 3 x 3 box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range (box_y * 3, box_y*3 + 3):
        for j in range (box_x * 3, box_x*3 + 3):
            if bo[i][j] == number and (i,j) != position:
                return False
   
    return True

#Function to print the board

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



# function to find an unsolved space in the board representing by (0)
def find_unsolved(bo): 
    
    for i in range (len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j]==0:
                return (i,j) # returning array number with unsolved piece

    return None


print_board(board)
backtrackSolve(board)
print("\n")
print ("THE SOLUTION FOR THE BOARD IS : ")
print_board(board)