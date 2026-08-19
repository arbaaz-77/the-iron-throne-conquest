# ⚔️ The Iron Throne Conquest

A text-based strategic simulation game built in Python, inspired by the Great Houses of Westeros.

This project demonstrates core software engineering fundamentals, including data structures (dictionaries and lists), graph traversal, game loop state management, and algorithmic combat resolution.

## ✨ Features

- **Dynamic Game State:** Tracks the military strength of the Great Houses of Westeros.
- **Geographic Traversal:** Implements an adjacency list (graph) to validate army movements across shared borders.
- **Randomized Combat:** Uses a custom algorithm combining base troop strength with RNG dice rolls to determine battle outcomes and allow for underdog victories.
- **Interactive Command Line:** A persistent game loop that sanitizes user input and handles invalid commands gracefully using guard clauses.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts:** Dictionaries, Lists, Functions, Control Flow (If/Else, While Loops), Input Sanitization, String Manipulation, Variable Scope.

## 🚀 How to Play

### Prerequisites

- Python 3.x installed on your local machine.

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone [https://github.com/arbaaz-77/the-iron-throne-conquest.git](https://github.com/arbaaz-77/the-iron-throne-conquest.git)
   ```

📜 Available Commands
The interactive prompt accepts the following commands. (Note: The command line is case-insensitive and handles accidental spaces automatically).

march [attacker] [defender] : Validates shared borders via the adjacency map and initiates combat between two existing houses. (Example: march Stark Lannister)

quit : Yields the Iron Throne and safely terminates the application loop.

- Developed by Arbaaz
