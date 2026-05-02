from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# ---------------- VALIDATION ----------------
def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row+i][start_col+j] == num:
                return False

    return True

# ---------------- SOLVER (CSP) ----------------
def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if solve(grid):
                            return True

                        grid[row][col] = 0
                return False
    return True

# ---------------- RANDOM SOLVER (for generation) ----------------
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def solve_random(grid):
    empty = find_empty(grid)
    if not empty:
        return True

    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)

    for num in nums:
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_random(grid):
                return True
            grid[row][col] = 0

    return False

# ---------------- GENERATOR ----------------
def generate_full_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_random(grid)
    return grid

def remove_numbers(grid, difficulty="easy"):
    if difficulty == "easy":
        remove_count = 30
    elif difficulty == "medium":
        remove_count = 40
    else:
        remove_count = 50

    puzzle = [row[:] for row in grid]

    while remove_count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            remove_count -= 1

    return puzzle

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve_sudoku():
    data = request.json
    grid = data["grid"]

    if solve(grid):
        return jsonify({"status": "solved", "grid": grid})
    else:
        return jsonify({"status": "no_solution"})

@app.route("/check", methods=["POST"])
def check():
    grid = request.json["grid"]

    for i in range(9):
        if len(set(grid[i])) != 9:
            return jsonify({"status": "fail"})

        col = [grid[j][i] for j in range(9)]
        if len(set(col)) != 9:
            return jsonify({"status": "fail"})

    return jsonify({"status": "success"})

@app.route("/generate", methods=["GET"])
def generate():
    full = generate_full_grid()
    puzzle = remove_numbers(full, "easy")

    return jsonify({
        "puzzle": puzzle,
        "solution": full
    })

# ---------------- RUN ----------------
if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)