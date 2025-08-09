#  Sudoku Solver with Python & Tkinter

A sleek and intuitive Sudoku solver with a graphical user interface built using Python. This application allows users to input any Sudoku puzzle and find its solution instantly using an efficient backtracking algorithm.


![Sudoku Solver Unsolved GUI](/Screenshots/unsolved.png)
*(A screenshot of the clean 9x9 grid interface with a sample puzzle entered)*

![Sudoku Solver Solved GUI](/Screenshots/solved.png)


---

## ✨ Features

* **Interactive 9x9 Grid:** A user-friendly grid designed with clear 3x3 box separations for easy number entry.
* **One-Click Solving:** Solves any valid Sudoku puzzle with the click of a single "Solve" button.
* **Intelligent Input Validation:**
    * Prevents the entry of non-numeric or out-of-range (1-9) values.
    * Validates the initial board state to ensure no rules are broken before solving.
* **Instant Feedback:** Displays clear error messages for invalid inputs or unsolvable puzzles.
* **Clear Board:** A "Clear" button to instantly reset the entire grid for a new puzzle.
* **Efficient Algorithm:** Utilizes a classic backtracking algorithm, implemented with NumPy for efficient board manipulation.

---

## 🚀 How to Use

1.  **Prerequisites:** Ensure you have Python installed on your system. The required libraries, **Tkinter** and **NumPy**, are typically included with standard Python distributions or can be installed via pip:
    ```bash
    pip install numpy
    ```

2.  **Run the Application:** Save the code as a Python file (e.g., `sudoku_gui.py`) and run it from your terminal:
    ```bash
    python sudoku_gui.py
    ```

3.  **Enter the Puzzle:** Click on any cell in the grid and type a number from 1 to 9. Fill in all the given numbers of your puzzle. Leave the cells you want the solver to fill in empty.

4.  **Solve:** Click the **"Solve"** button. The algorithm will run, and the solution will appear on the grid.

5.  **Clear:** Click the **"Clear"** button to erase all numbers from the grid and start over.

---

## 🛠️ Technologies Used

* **Language:** Python
* **GUI Library:** Tkinter
* **Numerical Operations:** NumPy

---

## 🧠 The Logic Behind the Solver

The core of this solver is a **backtracking algorithm**. Here's how it works in simple terms:

1.  **Find an Empty Cell:** The algorithm scans the board to find the next empty cell.
2.  **Try a Number:** It then tries to place a valid number (from 1 to 9) in that cell. A number is "valid" if it doesn't already exist in the same row, column, or 3x3 box.
3.  **Recurse:** If a valid number is found, it tentatively places it on the board and then calls itself to move on to the next empty cell.
4.  **Backtrack:** If it reaches a point where no valid numbers can be placed in a cell, it means a previous choice was wrong. It "backtracks" to the previously modified cell, erases the number it placed there, and tries the next valid number.
5.  **Solution:** This process continues until every cell is filled, at which point the puzzle is solved! If it tries all possibilities and can't find a solution, it concludes the puzzle is unsolvable.
# Sudoku-Solver
