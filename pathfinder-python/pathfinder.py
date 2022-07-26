from tkinter import messagebox, Tk
import pygame
import sys

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))

columns = 50
rows = 50

box_width = window_width // columns
box_height = window_height // rows

grid = []


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width,
                         self.y * box_height, box_width-2, box_height-2))


# create grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)

start_box = grid[0][0]
start_box.start = True


def main():
    begin_search = False
    target_box_set = False

    while True:
        for event in pygame.event.get():
          # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # mouse controls
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # draw the wall
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True
                    # set target
                    if event.buttons[2] and not target_box_set:
                        i = x // box_width
                        j = y // box_height
                        target_box = grid[i][j]
                        target_box.target = True
                        target_box_set = True
            # start algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True

        window.fill((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (50, 50, 50))
                if box.start:
                    box.draw(window, (0, 200, 200))
                if box.wall:
                    box.draw(window, (90, 90, 90))
                if box.target:
                    box.draw(window, (200, 200, 0))

        pygame.display.flip()


main()
