""""
    In this project, i implement the minimax algorithm to play 
    tictactoe. The user can choose a symbol X or O. If the user chooses the X
    symbol, then the AI will play as the O symbol and the other
    way around. The user has to enter the coordinates of the cell 
    he chooses.
"""

# Global Variables
minArray = []
maxArray = []
globalMINLevel = 0
globalMAXLevel = 0
globalPlayer = 0

# Print the current state
def PRINT_STATE(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()

def EMPTY_ARRAY(array):
    for i in range(len(array)):
        array.pop()

# Returns 1 if it's X's turn
# Returns -1 if it's O's turn
def PLAYER(state):
    Os = 0 
    Xs = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == "X":
                Xs+=1
            elif state[i][j] == "O":
                Os+=1

    if Xs>Os:
        return -1
    elif Os>=Xs:
        return 1
    return 1


# Returns all possible actions given the current state
def ACTIONS(state):
    actions = []
    row = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == "0":
                actions.append([])
                actions[row].append(i)
                actions[row].append(j)
                row+=1
    
    return actions


# Returns 1 if X wins
# Returns -1 if O wins
# Returns 0 if it's draw
def UTILITY(state):
    for i in range(3):
        if(state[i][0] == "X" and state[i][1] == "X" and state[i][2] == "X"):
            return 1
        if(state[i][0] == "O" and state[i][1] == "O" and state[i][2] == "O"):
            return -1

    for j in range(3):
        if(state[0][j] == "X" and state[1][j] == "X" and state[2][j] == "X"):
            return 1
        if(state[0][j] == "O" and state[1][j] == "O" and state[2][j] == "O"):
            return -1

    if(state[0][0] == "X" and state[1][1] == "X" and state[2][2] == "X"):
            return 1
    if(state[0][0] == "O" and state[1][1] == "O" and state[2][2] == "O"):
            return -1

    if(state[0][2] == "X" and state[1][1] == "X" and state[2][0] == "X"):
            return 1
    if(state[0][2] == "O" and state[1][1] == "O" and state[2][0] == "O"):
            return -1

    return 0


# Returns True if game is over
# Returns False if game is not over
def TERMINAL(state):
    gameover = UTILITY(state)
    if gameover == 1 or gameover == -1:
        return True

    # If there are any moves left then
    # the game is not over
    for i in range(3):
        for j in range(3):
            if state[i][j] == "0":
                return False
    return True


# Returns a new state afrer a certain action is taken
def RESULT(state,action,player):
    newState = [["0" for i in range(3)] for j in range(3)] 
    for i in range(3):
        for j in range(3):
            newState[i][j] = state[i][j]

    if player == -1:
        newState[action[0]][action[1]] = "O"
    elif player == 1:
        newState[action[0]][action[1]] = "X"

    return newState

def MAX_VALUE(state,player,globalMINLevel,globalMAXLevel):
    if TERMINAL(state) == True:
        return UTILITY(state)
    v = -10000
    for action in ACTIONS(state):
        v = max(v, MIN_VALUE(RESULT(state,action,player),player-2,globalMINLevel+1,globalMAXLevel))
        if globalPlayer == 1 and globalMAXLevel == 1:
            maxArray.append(v)
    return v

def MIN_VALUE(state,player,globalMINLevel,globalMAXLevel):
    if TERMINAL(state) == True:
        return UTILITY(state)
    v = 10000
    for action in ACTIONS(state):
        v = min(v, MAX_VALUE(RESULT(state,action,player),player+2,globalMINLevel,globalMAXLevel+1))
        if globalPlayer == -1 and globalMINLevel == 1:
            minArray.append(v)
    return v


def MINIMAX(state):
    player = globalPlayer
    newState = None
    if player == 1:
        MAX_VALUE(state,player,globalMINLevel,globalMAXLevel+1)
        action = ACTIONS(state)
        newState = RESULT(state,action[maxArray.index(max(maxArray))],globalPlayer)
        PRINT_STATE(newState)
        EMPTY_ARRAY(maxArray)
        return newState
    else:
        MIN_VALUE(state,player,globalMINLevel+1,globalMAXLevel)
        action = ACTIONS(state)
        newState = RESULT(state,action[minArray.index(min(minArray))],globalPlayer)
        PRINT_STATE(newState)
        EMPTY_ARRAY(minArray)
        return newState



state = [["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]]

print()
PRINT_STATE(state)

# In this game the X player plays first whether it's the user's turn or not
print("X player plays first")

# The player must choose the X symbol or the O symbol
print("Choose X or O")
HUMAN = input()
Xcoord = None
Ycoord = None
while True:
    # If the TERMINAL function return 1, break the loop
    if TERMINAL(state):
        break
    if PLAYER(state) == 1:
        # If the user chooses the X symbol execute this block of code
        if HUMAN == "X":
            # In order to make a move you need to enter both the x and y coordinates
            print("It's X's turn.")
            print()
            globalPlayer = 1
            print("Enter the x coordinate")
            Xcoord = int(input())
            print("Enter the y coordinate")
            Ycoord = int(input())
            state[Ycoord][Xcoord] = "X"
            PRINT_STATE(state)
            print()
        # Otherwise the AI plays
        else:
            print("It's X's turn.")
            print()
            globalPlayer = 1
            state = MINIMAX(state)
            print()

    else:
        # If the user chooses the O symbol execute this block of code
        if HUMAN == "O":
            # In order to make a move you need to enter both the x and y coordinates
            print("It's O's turn.")
            print()
            globalPlayer = -1
            print("Enter the x coordinate")
            Xcoord = int(input())
            print("Enter the y coordinate")
            Ycoord = int(input())
            state[Ycoord][Xcoord] = "O"
            PRINT_STATE(state)
            print()
        # Otherwise the AI plays
        else:
            print("It's O's turn.")
            print()
            globalPlayer = -1
            state = MINIMAX(state)
            print()