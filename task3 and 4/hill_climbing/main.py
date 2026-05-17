import random
import pygame
import time

N = 8
WINDOW_SIZE = 640
CELL_SIZE = WINDOW_SIZE // N

WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
RED = (200, 50, 50)
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("N-Queens Hill Climbing")

font = pygame.font.SysFont(None, 60)
def random_board():
    return [random.randint(0, N - 1) for _ in range(N)]
def heuristic(board):

    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if board[i] == board[j]:
                conflicts += 1

            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def neighbors(board):

    result = []

    for col in range(N):

        for row in range(N):

            if row != board[col]:

                neighbor = board.copy()
                neighbor[col] = row

                result.append(neighbor)

    return result

def draw_board(board, h):

    screen.fill((0, 0, 0))

    for row in range(N):
        for col in range(N):

            color = WHITE if (row + col) % 2 == 0 else BROWN

            pygame.draw.rect(
                screen,
                color,
                (col * CELL_SIZE, row * CELL_SIZE,
                 CELL_SIZE, CELL_SIZE)
            )
    for col in range(N):

        row = board[col]

        text = font.render("Q", True, RED)

        text_rect = text.get_rect(
            center=(
                col * CELL_SIZE + CELL_SIZE // 2,
                row * CELL_SIZE + CELL_SIZE // 2
            )
        )

        screen.blit(text, text_rect)

    pygame.display.set_caption(
        f"N-Queens Hill Climbing | Conflicts = {h}"
    )

    pygame.display.update()

def hill_climbing():

    current = random_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current_h = heuristic(current)

        draw_board(current, current_h)

        time.sleep(0.3)
        if current_h == 0:
            return current

        all_neighbors = neighbors(current)

        best_neighbor = current
        best_h = current_h

        for neighbor in all_neighbors:

            h = heuristic(neighbor)

            if h < best_h:

                best_neighbor = neighbor
                best_h = h

        if best_h >= current_h:

            print("Local optimum reached...")
            print("Restarting with random board...\n")

            current = random_board()

        else:
            current = best_neighbor

solution = hill_climbing()

print("\nSolution Found!")
print(solution)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()