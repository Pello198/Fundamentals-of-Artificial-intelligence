# N-Queens Problem Using Hill Climbing Algorithm

## Project Overview

This project solves the **N-Queens Problem** using the **Hill Climbing Algorithm** with **Random Restart** to avoid local optima.

The project also includes a **Pygame visualization** that displays:
- The chessboard
- Queen positions
- Conflict count during the search process

---

# What is the N-Queens Problem?

The N-Queens problem is a classic Artificial Intelligence and search problem.

The objective is to place **N queens** on an `N × N` chessboard such that:

- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

For this project:

```python
N = 8
```

So the program solves the **8-Queens Problem**.

---

# What is Hill Climbing?

Hill Climbing is a **local search algorithm** used in Artificial Intelligence.

The algorithm:
1. Starts with a random solution
2. Evaluates the solution using a heuristic function
3. Generates neighboring states
4. Moves to the best neighbor
5. Repeats until a solution is found

---

# Problem with Basic Hill Climbing

Basic Hill Climbing can become stuck in:
- Local optima
- Plateaus

This project solves that issue using:

# Random Restart Hill Climbing

If the algorithm gets stuck:
- It generates a new random board
- Starts searching again

This greatly improves the chances of finding a valid solution.

---

# Features

- Hill Climbing search algorithm
- Random Restart optimization
- Conflict heuristic function
- Chessboard visualization using Pygame
- Real-time animation of queen movement
- Displays current heuristic/conflict count

---

# Technologies Used

- Python
- Pygame

---



# Code Explanation

## 1. Random Board Generation

```python
def random_board():
```

Creates a random initial state.

Each index represents:
- a column

Each value represents:
- the queen’s row position

Example:

```python
[0, 4, 7, 5, 2, 6, 1, 3]
```

---

## 2. Heuristic Function

```python
def heuristic(board):
```

Calculates the number of attacking queen pairs.

Conflicts occur when queens:
- share the same row
- share the same diagonal

Goal state:

```python
heuristic(board) == 0
```

---

## 3. Neighbor Generation

```python
def neighbors(board):
```

Generates possible neighboring states by moving queens to different rows.

---

## 4. Hill Climbing Algorithm

```python
def hill_climbing():
```

Main search algorithm.

Steps:
1. Evaluate current board
2. Generate neighbors
3. Choose best neighbor
4. Move to better state
5. Restart if stuck

---

## 5. Visualization

```python
def draw_board(board, h):
```

Uses Pygame to:
- Draw chessboard
- Draw queens
- Display current conflict count

---

# Sample Output

Terminal:

```text
Local optimum reached...
Restarting with random board...

Solution Found!
[0, 4, 7, 5, 2, 6, 1, 3]
```

Visualization:
- Animated chessboard
- Red queens moving toward solution

---

# Heuristic Formula

The heuristic counts attacking pairs of queens.

Lower heuristic values are better.

Goal:

```text
h(n) = 0
```

---

# Advantages of Hill Climbing

- Simple to implement
- Memory efficient
- Faster than brute force search
- Works well for optimization problems

---

# Limitations

- Can get stuck in local optima
- Not guaranteed to find global optimum without restart
- Performance depends on starting state

---

# Improvements Used

This project improves basic Hill Climbing using:

## Random Restart

When stuck:
- Generate a new random board
- Continue searching

This significantly improves success rate.

---