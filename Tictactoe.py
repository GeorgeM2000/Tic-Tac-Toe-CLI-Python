""""
    In this project, i implement the minimax algorithm to play 
    tictactoe. The user can choose a symbol X or O. If the user chooses the X
    symbol, then the AI will play as the O symbol and the other
    way around. The user has to enter the coordinates of the cell 
    he chooses.
"""
class Tictactoe:

    def __init__(self):
        self.max_array = []
        self.min_array = []

        self.x_top_level = 0
        self.o_top_level = 0

        self.player = 0


    # Print the current state
    def PRINT_STATE(self, state):
        for i in range(3):
            for j in range(3):
                print(state[i][j], end=" ")
            print()

    def EMPTY_ARRAY(self, array):
        for i in range(len(array)):
            array.pop()

    # Returns 1 if it's X's turn
    # Returns -1 if it's O's turn
    def PLAYER(self, state):
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
    def ACTIONS(self, state):
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
    def UTILITY(self, state):
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
    def TERMINAL(self, state):
        gameover = self.UTILITY(state)
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
    def RESULT(self, state, action, player):
        newState = [["0" for i in range(3)] for j in range(3)] 
        for i in range(3):
            for j in range(3):
                newState[i][j] = state[i][j]

        if player == -1:
            newState[action[0]][action[1]] = "O"
        elif player == 1:
            newState[action[0]][action[1]] = "X"

        return newState

    # MAX_VALUE
    def MAX_VALUE(self, state, o_top_level, x_top_level):
        if self.TERMINAL(state):
            return self.UTILITY(state)

        v = -10000
        for action in self.ACTIONS(state):
            res = self.MIN_VALUE(self.RESULT(state, action, 1), o_top_level+1, x_top_level)
            v = max(v, res)
            if self.player == 1 and x_top_level == 1:
                self.max_array.append(res)
        return v

    # MIN_VALUE
    def MIN_VALUE(self, state, o_top_level, x_top_level):
        if self.TERMINAL(state):
            return self.UTILITY(state)

        v = 10000
        for action in self.ACTIONS(state):
            res = self.MAX_VALUE(self.RESULT(state, action, -1) , o_top_level, x_top_level+1)
            v = min(v, res)
            if self.player == -1 and o_top_level == 1:
                self.min_array.append(res)
        return v

    # MINIMAX
    def MINIMAX(self,state, player):
        if player == 1:
            self.player = 1
            self.MAX_VALUE(state, self.o_top_level, self.x_top_level+1)
            action = self.ACTIONS(state)
            newState = self.RESULT(state, action[self.max_array.index(max(self.max_array))],1)
            

            self.PRINT_STATE(newState)
            self.EMPTY_ARRAY(self.max_array)
            return newState
        else:
            self.player = -1
            self.MIN_VALUE(state, self.o_top_level+1, self.x_top_level)
            action = self.ACTIONS(state)
            newState = self.RESULT(state,action[self.min_array.index(min(self.min_array))],-1)
            

            self.PRINT_STATE(newState)
            self.EMPTY_ARRAY(self.min_array)
            return newState


if __name__ == "__main__":

    state = [  

        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]

            ]

    Tictactoe_Solver = Tictactoe()

    print()
    Tictactoe_Solver.PRINT_STATE(state)

    # In this game the X player plays first whether it's the user's turn or not
    print("X player plays first")

    # The player must choose the X symbol or the O symbol
    print("Choose X or O")
    HUMAN = input()
    Xcoord = None
    Ycoord = None
    while True:

        # If the TERMINAL function return 1, break the loop
        if Tictactoe_Solver.TERMINAL(state):
            winner = Tictactoe_Solver.UTILITY(state)
            if winner == 1:
                print("X Wins!")
            elif winner == -1:
                print("O Wins!")
            else:
                print("Tie!")
            break
        
        if Tictactoe_Solver.PLAYER(state) == 1:
            # If the user chooses the X symbol execute this block of code
            if HUMAN == "X":
                # In order to make a move you need to enter both the x and y coordinates
                print("It's X's turn.")
                print()
                print("Enter the x coordinate")
                Xcoord = int(input())
                print("Enter the y coordinate")
                Ycoord = int(input())
                state[Ycoord][Xcoord] = "X"
                Tictactoe_Solver.PRINT_STATE(state)
                print()
            # Otherwise the AI plays
            else:
                print("It's X's turn.")
                print()
                state = Tictactoe_Solver.MINIMAX(state, 1)
                print()

        else:
            # If the user chooses the O symbol execute this block of code
            if HUMAN == "O":
                # In order to make a move you need to enter both the x and y coordinates
                print("It's O's turn.")
                print()
                print("Enter the x coordinate")
                Xcoord = int(input())
                print("Enter the y coordinate")
                Ycoord = int(input())
                state[Ycoord][Xcoord] = "O"
                Tictactoe_Solver.PRINT_STATE(state)
                print()
            # Otherwise the AI plays
            else:
                print("It's O's turn.")
                print()
                state = Tictactoe_Solver.MINIMAX(state, -1)
                print()