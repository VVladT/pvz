import random

from app.constants import SPRITES, TILE_SIZE
from app.entities.sprite import Sprite
import pygame

class Board:
    timer = 0

    def __init__(self, spritesheet, dimension=(8,5), pos=(10,32)):
        self.cols = dimension[0]
        self.rows = dimension[1]
        self.x = pos[0]
        self.y = pos[1]
        self.tile_size = TILE_SIZE
        self.spritesheet = spritesheet
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.hover_pos = None
        self.variants = []
        for pos in SPRITES["grass"]["variants"]:
            data = {
                "frames": [pos],
                "size": SPRITES["grass"]["size"]
            }
            self.variants.append(Sprite(data["frames"][0], data["size"], spritesheet))

    def update_hover(self, mouse_pos):
        if mouse_pos is None:
            self.hover_pos = None
            return

        col = (mouse_pos[0] - self.x) // self.tile_size
        row = (mouse_pos[1] - self.y) // self.tile_size

        if 0 <= col < self.cols and 0 <= row < self.rows:
            self.hover_pos = (col, row)

    def update_plants(self, dt):
        self.timer += dt

        for row in range(self.rows):
            for col in range(self.cols):
                plant = self.grid[row][col]
                if plant is not None:
                    if plant.type == "offensive":
                        if self.timer >= .4:
                            if random.random() < 0.5:
                                plant.update_state("shooting")
                            else:
                                plant.update_state("idle")
                    if plant.type == "sun_producer":
                        if self.timer >= .4:
                            if random.random() < 0.15:
                                plant.update_state("producing")
                            else:
                                plant.update_state("idle")
                    if plant.type == "defensive":
                        plant.update_state("full")
                    if plant.type == "instantaneous":
                        if self.timer >= .4:
                            plant.update_state()

        if self.timer >= .4:
            self.timer = 0


    def draw(self, surface):
        green = (0, 228, 54)
        board_rect = pygame.Rect(
            self.x,
            self.y,
            self.cols * self.tile_size,
            self.rows * self.tile_size
        )
        pygame.draw.rect(surface, green, board_rect)

        for row in range(self.rows):
            for col in range(self.cols):
                x = self.x + col * self.tile_size
                y = self.y + row * self.tile_size

                if (row + col) % 2 == 0:
                    index = (row * self.cols + col) % len(self.variants)
                    variant = self.variants[index]
                    variant.draw(surface, (x, y))

                if self.grid[row][col] is None and self.hover_pos == (col, row):
                    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(x-1, y-1, self.tile_size + 2, self.tile_size + 2), 1)
                if self.grid[row][col] is not None:
                    self.grid[row][col].draw(surface, (x, y))