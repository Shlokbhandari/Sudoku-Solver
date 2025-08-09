import numpy as np
import tkinter as tk
from tkinter import messagebox
#---------------------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.title("Sudoku Solver")

frame = tk.Frame(window)
frame.pack()

cells = [[None for _ in range(9)] for _ in range(9)]
for box_row in range(3):
    for box_col in range(3):
        box_frame = tk.Frame(frame, borderwidth=2, relief='solid')
        box_frame.grid(row=box_row, column=box_col)
        for r_in_box in range(3):
            for c_in_box in range(3):
                abs_row = box_row * 3 + r_in_box
                abs_col = box_col * 3 + c_in_box
                cell = tk.Entry(box_frame, width=4, font=('Arial', 18), justify='center')
                cell.grid(row=r_in_box, column=c_in_box)
                cells[abs_row][abs_col] = cell

def clear_board():
    for r in range(9):
        for c in range(9):
            cells[r][c].delete(0, tk.END)
            
def solve_gui():
    puzzle = []
    for r in range(9):
        row = []
        for c in range(9):
            val = cells[r][c].get()

            if val == "":
                row.append(0)
                continue

            
            if not val.isdigit() or not (1 <= int(val) <= 9):
                messagebox.showerror("Input Error", f"Invalid value '{val}' found. Please use single digits from 1-9.")
                return 
            
            row.append(int(val))
        puzzle.append(row)

    puzzle_board = np.array(puzzle)

    if is_board_valid(puzzle_board):
        if solve(puzzle_board):
            for r in range(9):
                for c in range(9):
                    cells[r][c].delete(0, tk.END)
                    cells[r][c].insert(0, puzzle_board[r, c])
        else:
            messagebox.showerror("Unsolvable", "This puzzle has no solution.")
    else:
        
        messagebox.showerror("Validation error","Invalid board setup.")

button_frame = tk.Frame(window)
button_frame.pack()

solve_button = tk.Button(button_frame, text="Solve", font=('Arial', 14), command=solve_gui)
clear_button = tk.Button(button_frame, text="Clear", font=('Arial', 14), command=clear_board)

solve_button.grid(row=0, column=0, padx=10, pady=10)
clear_button.grid(row=0, column=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------------
def is_valid(board, row, col, num):
    for x in board[row,:]:
        if x == num:
            return False
    for x in board[:,col]:
        if x == num:
            return False
    st_row = (row//3)*3
    st_col = (col//3)*3
    if num in board[st_row:st_row+3,st_col:st_col+3]:
        return False
    return True

def is_board_valid(board):
    for r in range(9):
        for c in range(9):
            if board[r,c]!=0:
                a = board[r,c]
                board[r,c] = 0
                if is_valid(board, r , c, a) == False:
                    board[r,c] = a
                    return False
                board[r,c] = a
    return True
    
def empty(board):
    for r in range(9):
        for c in range(9):
            if board[r,c] == 0:
                return (r,c)
    return None
    
def solve(board):
    find = empty(board)
    if find == None:
        return True
    else:
        row,col = find
        
    for i in range(1,10):
        if is_valid(board, row, col, i):
            board[row,col] = i
            if solve(board):
                return True
            board[row,col] = 0
    return False


window.mainloop()
