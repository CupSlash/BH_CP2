import pygame
import random
pygame.init()
WIDTH, HEIGHT = 400,400
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush")
grid = [[random.randint(1,3) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
selected_candy = None
def handle_click(row, col):
    global selected_candy
    if selected_candy is None:
        selected_candy = (row,col)
    else:
        row1, col1 = selected_candy
        grid[row][col], grid[row1][col1] = grid[row1][col1], grid[row][col]
        selected_candy = None
def detect_match():
    matches = set()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2):
            if grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                matches.add((row,col))
                matches.add((row, col + 1))
                matches.add((row, col + 2))
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2):
            if grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                matches.add((row,col))
                matches.add((row + 1, col))
                matches.add((row + 2, col))
    return matches
def fill_empty_spaces():
    for col in range(GRID_SIZE):
        empty_count = sum(1 for row in range(GRID_SIZE) if grid[row][col] == 0)
        for _ in range(empty_count):
            grid[GRID_SIZE - 1][_] = random.randint(1,3)
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_SIZE
            row = event.pos[1] // CELL_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                handle_click(row, col)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            candy_type = grid[row][col]
            if candy_type == 1:
                candy_color = (255,0,0) 
            elif candy_type == 2:
                candy_color = (0,255,0)
            elif candy_type == 3:
                candy_color = (0,0,255) 
            else:
                candy_color = (0,0,0)
            pygame.draw.rect(screen, candy_color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    matches = detect_match()
    if matches:
        for row, col in matches:
            grid[row][col] = 0
    pygame.display.flip()
pygame.quit()