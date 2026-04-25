const gridElement = document.getElementById("grid");

// Create grid
for (let i = 0; i < 81; i++) {
    let input = document.createElement("input");
    input.maxLength = 1;

    input.addEventListener("input", () => {
        input.value = input.value.replace(/[^1-9]/g, "");
    });

    gridElement.appendChild(input);
}

// Popup logic
let popupTimeout;

function showPopup(message) {
    const popup = document.getElementById("popup");
    const msg = document.getElementById("popup-message");

    msg.innerText = message;
    popup.classList.remove("hidden");

    clearTimeout(popupTimeout);
    popupTimeout = setTimeout(closePopup, 3000);
}

function closePopup() {
    document.getElementById("popup").classList.add("hidden");
}

// Get grid
function getGrid() {
    let inputs = document.querySelectorAll("#grid input");
    let grid = [];

    for (let i = 0; i < 9; i++) {
        let row = [];
        for (let j = 0; j < 9; j++) {
            let val = inputs[i * 9 + j].value;
            row.push(val ? parseInt(val) : 0);
        }
        grid.push(row);
    }
    return grid;
}

// Set grid
function setGrid(grid) {
    let inputs = document.querySelectorAll("#grid input");

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            inputs[i * 9 + j].value = grid[i][j] !== 0 ? grid[i][j] : "";
        }
    }
}

// Solve
async function solveSudoku() {
    let res = await fetch("/solve", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({grid: getGrid()})
    });

    let data = await res.json();

    if (data.status === "solved") {
        setGrid(data.grid);
        showPopup("Solved ✅");
    } else {
        showPopup("No Solution ❌");
    }
}

// Check
async function checkSudoku() {
    let res = await fetch("/check", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({grid: getGrid()})
    });

    let data = await res.json();

    if (data.status === "success") {
        showPopup("You won 🎉");
    } else {
        showPopup("Try again ❌");
    }
}

// Generate
async function generatePuzzle() {
    let res = await fetch("/generate");
    let data = await res.json();

    setGrid(data.puzzle);
    showPopup("New Puzzle Loaded 🧩");
}

// Clear
function clearGrid() {
    document.querySelectorAll("#grid input").forEach(i => i.value = "");
    showPopup("Cleared 🧹");
}