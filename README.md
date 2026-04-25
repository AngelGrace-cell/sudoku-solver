# 🧩 Sudoku Solver

A web-based Sudoku game built using **Constraint Satisfaction Problem (CSP)** techniques with an interactive UI.


## 📌 Problem Description

Sudoku is a logic-based number placement puzzle played on a 9×9 grid. Some cells are pre-filled, and the objective is to fill the remaining cells such that:

- Each row contains digits **1–9 without repetition**
- Each column contains digits **1–9 without repetition**
- Each 3×3 subgrid contains digits **1–9 without repetition**

This project provides:
- An interactive Sudoku interface  
- Automatic puzzle generation  
- Solution validation  
- A CSP-based solver  


## 🧠 Algorithms Used

### 🔹 1. Constraint Satisfaction Problem (CSP)
Sudoku is modeled as a CSP:
- **Variables** → Empty cells  
- **Domain** → Values {1–9}  
- **Constraints**:
  - Unique values in each row  
  - Unique values in each column  
  - Unique values in each 3×3 subgrid  


### 🔹 2. Backtracking Algorithm
A recursive approach:
1. Find an empty cell  
2. Try numbers from 1–9  
3. Check constraints  
4. If valid → continue  
5. If invalid → backtrack  


### 🔹 3. Randomized Backtracking (Puzzle Generator)
- Generate a complete valid Sudoku grid  
- Randomly remove numbers to create a playable puzzle  


## ▶️ Execution Steps

1. Open the project in a code editor (such as VS Code).  
2. Ensure Python is installed on the system.  
3. Install the required dependencies listed in `requirements.txt`.  
4. Run the main application file to start the server.  
5. Open a web browser and navigate to the local server URL.  
6. Use the interface to:
   - Generate a new Sudoku puzzle  
   - Enter values into the grid  
   - Solve the puzzle automatically  
   - Check your solution  


## 🎮 Features

- 🧩 Generate Sudoku puzzles  
- 🧠 Solve using CSP (Backtracking)  
- ✅ Validate user input  
- ✨ Popup-based feedback system  
- 🎨 Modern UI  


## 🛠 Tech Stack

- Python (Flask)  
- HTML, CSS, JavaScript  
