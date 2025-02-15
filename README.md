# Tic-Tac-Toe Game – CS50 Python Final Project  

Hello, my name is **Artur Jodkowski**, and this is my **CS50 Python final project**.  
This project is a **Tic-Tac-Toe game** with multiple difficulty levels and an AI opponent.  

---

## 1. About the Project

This project is a digital version of the classic **Tic-Tac-Toe** game, where the player competes against an AI-controlled opponent. The game offers four difficulty levels, ranging from beginner to expert, providing both entertainment and challenge. The AI's behavior changes depending on the difficulty level, from simple random moves to using advanced algorithms such as the **Minimax algorithm** for perfect gameplay.

The game logic is designed to be modular, making it easy to maintain and extend. Additionally, automated tests have been created to ensure the correctness of the core functions.

---

## 2. How the Game Works

### a) Welcome Screen
- When you run the program, a welcome message appears. The message introduces the game and prompts you to press **ENTER** to continue.
- The welcome screen is displayed using the `tabulate` and `pyfiglet` libraries to make the output more visually appealing.

### b) Difficulty Selection
- After the welcome message, you are prompted to select one of the four difficulty levels:
  - **Easy:** The AI makes random moves.  
  - **Medium:** The AI blocks your winning moves if possible.  
  - **Hard:** The AI tries to win first and blocks you if it cannot win immediately.  
  - **Impossible:** The AI uses the **Minimax algorithm**, making it unbeatable.

### c) Board Size Selection
- Next, you are prompted to select the size of the game board. The game allows you to play not only on the standard 3x3 board but also on larger boards (e.g., 4x4, 5x5).

### d) Gameplay
- You always play as **X (crosses)**. The AI plays as **O (circles)** or a green circle symbol.  
- You make a move by entering the number of the cell you wish to mark. The cells are numbered from **1 to N²**, depending on the board size.  
- The game board is updated and displayed after every move using the `tabulate` library.  
- The game continues until there is a winner or the board is full (resulting in a draw).  

### e) Game Results and Replay
- When the game ends, the program displays the result:
  - **You Win:** If you complete a row, column, or diagonal with your marks.  
  - **Computer Wins:** If the AI completes a winning combination.  
  - **Draw:** If there are no moves left and no winner.  

- After showing the result, the program asks if you would like to play again. You can type **Y** to restart or **N** to exit the game.

---

## 3. Difficulty Levels and AI Logic

The AI behavior is defined differently for each difficulty level:

### 1. Easy  
The AI chooses the first available cell without any strategy.  
*This is implemented in `level_1_easy.py`.*

### 2. Medium  
The AI tries to block your winning moves. It checks each row, column, and diagonal to see if you are one move away from winning.  
*This logic is implemented in `level_2_medium.py`.*

### 3. Hard  
The AI first tries to win if possible. If it cannot win immediately, it blocks your winning moves. This is an improvement over the medium level.  
*This logic is implemented in `level_3_hard.py`.*

### 4. Impossible (Minimax Algorithm)  
The AI uses the **Minimax algorithm**, which is a backtracking algorithm that evaluates every possible move and chooses the one that guarantees the best outcome. With this algorithm, the AI becomes unbeatable.  
*This logic is implemented in `level_4_impossible.py`.*

---

## 4. Project Structure

The project is organized into multiple files for modularity and clarity:

```plaintext
Tic-Tac-Toe/
├── project.py              # Main program with game loop
├── messages.py             # Displays welcome, results, and replay messages
├── level_1_easy.py         # Easy AI logic (random moves)
├── level_2_medium.py       # Medium AI logic (blocks player's winning moves)
├── level_3_hard.py         # Hard AI logic (tries to win or block)
├── level_4_impossible.py   # Impossible AI logic (Minimax algorithm)
├── test_project.py         # Automated tests for game functions
└── requirements.txt        # List of required Python libraries
