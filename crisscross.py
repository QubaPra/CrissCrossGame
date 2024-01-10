import random
import os

symbols = ["▲", "X", "/", "#", "O", "="]
board = [["[ ]" for _ in range(5)] for _ in range(5)]
randomSymbol1 = " "
randomSymbol2 = " "

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printBoard():
    for row in board:
        print("".join(row))

def generateSymbols():
    global randomSymbol1, randomSymbol2
    randomSymbol1 = random.choice(symbols)
    randomSymbol2 = random.choice(symbols)
     

def placeSymbols():
    global randomSymbol1, randomSymbol2
    print(f"Place these symbols on the board: {randomSymbol1} and {randomSymbol2}\n") 
    printBoard()      

    print(f"\nPlace {randomSymbol1} on the board:")
    row1 = int(input("Enter the row number: "))
    col1 = int(input("Enter the column number: "))

    print(f"\nPlace {randomSymbol2} on the board:")
    row2 = int(input("Enter the row number: "))
    col2 = int(input("Enter the column number: "))

    # Check if the second symbol can be placed next to the first symbol
    if 0 <= row1 < len(board) and 0 <= col1 < len(board[0]) and 0 <= row2 < len(board) and 0 <= col2 < len(board[0]):
        # Check if the row and column are within the board
        if board[row1][col1] == "[ ]" and board[row2][col2] == "[ ]":
            # Check if the position is already occupied by a symbol
            if (row2 == row1 and abs(col2 - col1) == 1) or (col2 == col1 and abs(row2 - row1) == 1):
                board[row1][col1] = f"[{randomSymbol1}]"
                board[row2][col2] = f"[{randomSymbol2}]"
            else:
                cls()
                print("\033[91mInvalid placement. The second symbol must be placed next to the first symbol. Try again.\033[0m")
                placeSymbols()
        else:
            cls()
            print("\033[91mInvalid placement. The position is already occupied. Try again.\033[0m")
            placeSymbols()
    else:
        cls()
        print("\033[91mInvalid placement. The position is outside the board. Try again.\033[0m")
        placeSymbols()
    cls()

def checkEmptyAdjacent():
    for row in range(len(board)):
        for col in range(len(board[0])):
            if col < len(board[0]) - 1 and board[row][col] == "[ ]" and board[row][col+1] == "[ ]":
                return True
            if row < len(board) - 1 and board[row][col] == "[ ]" and board[row+1][col] == "[ ]":
                return True
    return False

def addPoints(count):
    if count == 1:
        return 0
    elif count == 2:
        return 2
    elif count == 3:
        return 3
    elif count == 4:
        return 8
    elif count == 5:
        return 10

def result():
    points = 0

    # Add points for rows
    for row in range(0, len(board)):
        rowPoints = 0
        count = 1
        for col in range(0, len(board)-1):
            if board[row][col] == board[row][col+1] and board[row][col] != "[ ]":
                count += 1
            else:
                rowPoints += addPoints(count)
                count = 1
        rowPoints += addPoints(count)
        if rowPoints == 0:
            points -= 5
        else:
            points += rowPoints
    
    # Add points for columns
    for col in range(0, len(board)):
        colPoints = 0
        count = 1
        for row in range(0, len(board)-1):
            if board[row][col] == board[row+1][col] and board[row][col] != "[ ]":
                count += 1
            else:
                colPoints += addPoints(count)
                count = 1
        colPoints += addPoints(count)
        if colPoints == 0:
            points -= 5
        else:
            points += colPoints
        
    # Add points for diagonal
    count = 1 
    diagonalPoints = 0
    for col in range(0, len(board)-1):              
        if board[4-col][col] == board[4-col-1][col+1] and board[4-col][col] != "[ ]":
            count += 1
        else:
            diagonalPoints += addPoints(count)*2
            count = 1
    diagonalPoints += addPoints(count)*2
    if diagonalPoints == 0:
        points -= 5*2
    else:
        points += diagonalPoints
    
    return points

cls()
print("\033[92mWelcome to Criss Cross!\033[0m")
input("Press enter to continue...")
cls()

print("Which symbol would you like to place at start position (0,0)?")
symbol = input().capitalize()
if symbol == "T": 
        symbol = "▲"
while symbol not in symbols:
    print("\033[91mInvalid symbol. Please try again.\033[0m")
    symbol = input().capitalize()    
board[0][0] = f"[{symbol}]"
cls()



while checkEmptyAdjacent():
    generateSymbols()
    placeSymbols()

printBoard()
print(f"\033[92mCongratulations! You got {result()} points\033[0m")
