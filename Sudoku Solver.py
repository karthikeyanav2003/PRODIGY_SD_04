import tkinter as tk
from tkinter import messagebox, simpledialog

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Check if num is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(4)]:
        return False

    # Check if num is not in the same 2x2 subgrid
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(2):
        for j in range(2):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 5):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.custom_puzzle_button = tk.Button(root, text="Enter Custom Puzzle", command=self.enter_custom_puzzle)
        self.custom_puzzle_button.pack(pady=10)

        self.solve_button = tk.Button(root, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.pack(pady=10)

        self.sudoku_board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [2, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

    def print_sudoku(self, board):
        for row in board:
            print(" ".join(map(str, row)))

    def enter_custom_puzzle(self):
        user_input = simpledialog.askstring("Input", "Enter the Sudoku puzzle row-wise (use 0 for empty cells):")
        user_input = [int(char) for char in user_input.replace(" ", "")]

        if len(user_input) == 16:
            self.sudoku_board = [user_input[i:i + 4] for i in range(0, 16, 4)]
            messagebox.showinfo("Info", "Custom puzzle set successfully!")
        else:
            messagebox.showerror("Error", "Invalid input length. Please enter exactly 16 digits.")

    def solve_puzzle(self):
        print("\nUnsolved Sudoku:")
        self.print_sudoku(self.sudoku_board)

        if solve_sudoku(self.sudoku_board):
            print("\nSolved Sudoku:")
            self.print_sudoku(self.sudoku_board)
        else:
            print("\nNo solution exists.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
