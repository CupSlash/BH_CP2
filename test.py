import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 6
CELL_SIZE = WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treat Trios!")

grid = [[random.randint(1, 3) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
selected_candy = None

def handle_click(row, col):
    global selected_candy
    if selected_candy is None:
        selected_candy = (row, col)
    else:
        row1, col1 = selected_candy
        grid[row][col], grid[row1][col1] = grid[row1][col1], grid[row][col]
        selected_candy = None

def detect_match():
    matches = set()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                matches.update([(row, col), (row, col + 1), (row, col + 2)])
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2):
            if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                matches.update([(row, col), (row + 1, col), (row + 2, col)])
    return matches

def fill_empty_spaces():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                grid[row][col] = random.randint(1, 3)

running = True
while running:
    screen.fill((255, 255, 255)) # Clear screen to white
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_SIZE
            row = event.pos[1] // CELL_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                handle_click(row, col)

    matches = detect_match()
    if matches:
        for r, c in matches:
            grid[r][c] = 0
        fill_empty_spaces()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            candy_type = grid[row][col]
            if candy_type == 1:
                color = (255, 0, 0) # Red
            elif candy_type == 2:
                color = (0, 255, 0) # Green
            elif candy_type == 3:
                color = (0, 0, 255) # Blue
            else:
                color = (255, 255, 255) # White
            
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
            
            if selected_candy == (row, col):
                pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    pygame.display.flip()

pygame.quit()
