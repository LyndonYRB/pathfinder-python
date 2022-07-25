from tkinter import messagebox, Tk
from turtle import window_height, window_width
import pygame
import sys

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))

columns = 25
rows = 25

box_width = window_width // columns
box_height = window_height // rows

grid = []


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width,
                         self.y * box_height, box_width-2, box_height-2))


# create grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)


def main():
    while True:
        for event in pygame.event.get():
          # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (20, 20, 20))

        pygame.display.flip()


main()
