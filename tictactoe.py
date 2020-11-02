from random import randrange
import time
board = [[1,2,3],[4,5,6],[7,8,9]]
victor = None

def DisplayBoard(board):
    print("+" + 7*"-" + "+" + 7*"-" + "+" + 7*"-" + "+")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("|" + 3*" " + str(board[0][0]) + 3*" " + \
          "|" + 3*" " + str(board[0][1]) + 3*" " + \
          "|" + 3*" " + str(board[0][2]) + 3*" " + "|")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("+" + 7*"-" + "+" + 7*"-" + "+" + 7*"-" + "+")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("|" + 3*" " + str(board[1][0]) + 3*" " + \
          "|" + 3*" " + str(board[1][1]) + 3*" " + \
          "|" + 3*" " + str(board[1][2]) + 3*" " + "|")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("+" + 7*"-" + "+" + 7*"-" + "+" + 7*"-" + "+")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("|" + 3*" " + str(board[2][0]) + 3*" " + \
          "|" + 3*" " + str(board[2][1]) + 3*" " + \
          "|" + 3*" " + str(board[2][2]) + 3*" " + "|")
    time.sleep(0.04)
    print("|" + 7*" " + "|" + 7*" " + "|" + 7*" " + "|")
    time.sleep(0.04)
    print("+" + 7*"-" + "+" + 7*"-" + "+" + 7*"-" + "+")

def EnterMove(board):
    while True:
        move = int(input("Enter your move: ")) 
        if move < 1 or move > 9:
            print("Please enter a valid number (1-9)")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        if board[row][col] not in ["X", "O"]:
            board[row][col] = "O"
            break
        else:
            print("Field occupied. Try again.")
            continue
        
def MakeListOfFreeFields(board):
    free_fields = []
    for row in range(3):
        for i in range(3):
            if board[row][i] not in ["O", "X"]:
                free_fields.append((row, i))
    return free_fields
    
def VictoryFor(board, sign):
    if sign == "X":
        potential = "cpu"
    elif sign == "O":
        potential = "player"
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return potential
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return potential
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return potential
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return potential
    else:
        return None
    

def DrawMove(board):
    from random import randrange
    print("CPU is thinking........")
    time.sleep(5
               )
    while True:
        cpu_row = randrange(3)
        cpu_col = randrange(3)
        if board[cpu_row][cpu_col] == "X" or board[cpu_row][cpu_col] == "O":
            continue
        else:
            board[cpu_row][cpu_col] = "X"
            break

board[1][1] = "X"
turn = True
while victor == None:
    free = MakeListOfFreeFields(board)
    DisplayBoard(board)
    if free == []:
        victor = "tie"
    elif turn == True:
        EnterMove(board)
        victor = VictoryFor(board, "O")
        turn = not turn
        continue
    elif turn == False:
        DrawMove(board)
        victor = VictoryFor(board, "X")
        turn = not turn
        continue
    

if victor == "player":
    DisplayBoard(board)
    print("Congratulations! You win.")
elif victor == "cpu":
    DisplayBoard(board)
    print("You have lost!")
else:
    print("It's a tie!")
    
close = input("Press any key to exit.")
        
        


