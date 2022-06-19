from stack_array import Stack
#from stack_linked import Stack

import copy

def main():
    n = int(input("Enter n: "))
    max_solutions = int(input("Enter max solutions (-1 for inf): "))
    debug = input("Debug mode (y/n): ").lower()=="y"
    solve_nqueens(n,max_solutions,debug)

def solve_nqueens(n,max_solutions=-1,debug=False):
    found_solutions = 0
    my_stack = Stack()
    new_board = BoardState(n)
    my_stack.push(new_board)

    while not my_stack.is_empty() and (found_solutions < max_solutions or max_solutions == -1):
        popped_board = my_stack.pop()
        if debug == True:
            popped_board.display()
            input()
            
        if popped_board.is_solved():
            popped_board.display(True)
            found_solutions += 1
        else:
            for board in popped_board.explore_state():
                my_stack.push(board) 

    print(f"{found_solutions} solutions found.")
        

class BoardState:

    def __init__(self,n):
        self.board = []

        for i in range(n):
            self.board.append([])
        for row in self.board:
            for i in range(n):
                row.append("_")
    
    def display(self,queens_only=False):
        if queens_only == False:
            for row in self.board:
                for item in row:
                    print(item, end=" ")
                print()

        if queens_only == True:
            for row in self.board:
                for item in row:
                    if item == "Q":
                        print("Q", end=" ")
                    else:
                        print("_", end=" ")
                print()
        print()
    
    def clone(self):
        copy_board = copy.deepcopy(self)
        return copy_board
        
    def is_solved(self):
        for row in self.board:
            if "Q" not in row:
                return False
        return True
    
    def explore_state(self):
        return_boards = []
        row = 0
        col = 0
        no_queen = False

        while row < len(self.board) and no_queen == False:
            if "Q" not in self.board[row]:
                no_queen = True
                while col < len(self.board[row]):
                    if self.board[row][col] == "_":
                        new_board = self.clone()
                        new_board.place_queen(row,col)
                        return_boards.append(new_board)
                    col += 1
            row += 1
        return return_boards
        
    def place_queen(self,row,col):
        self.board[row][col] = "Q"
        start_row = copy.deepcopy(row)
        start_col = copy.deepcopy(col)
                
        while row < len(self.board)-1 and col > 0:
            row += 1
            col -= 1
            self.board[row][col] = "/"
        row = start_row
        col = start_col

        while row < len(self.board)-1:
            row += 1
            self.board[row][col] = "|"
        row = start_row
        col = start_col

        while row < len(self.board)-1 and col < len(self.board[row])-1:
            row += 1
            col += 1
            self.board[row][col] = "\\"
        


if __name__ == "__main__":
    main()
