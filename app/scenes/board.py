from app.core.constants import DATA, TILE_SIZE
from app.entities.sprite import Sprite
import pygame


class Board:
    def __init__(self, context, dimension=(8, 5), pos=(10, 32)):
        self.cols = dimension[0]
        self.rows = dimension[1]
        self.x = pos[0]
        self.y = pos[1]
        self.tile_size = TILE_SIZE
        self.context = context
        self.hover_pos = None

        self.variants = []
        for pos in DATA["grass"]["variants"]:
            data = {
                "frames": [pos],
                "size": DATA["grass"]["size"]
            }
            self.variants.append(Sprite(data["frames"][0], data["size"], context.spritesheet))

    def update_hover(self, mouse_pos):
        if mouse_pos is None:
            self.hover_pos = None
            return

        col = (mouse_pos[0] - self.x) // self.tile_size
        row = (mouse_pos[1] - self.y) // self.tile_size

        if 0 <= col < self.cols and 0 <= row < self.rows:
            if self.get_plant_at(col, row) is None:
                self.hover_pos = (col, row)
            else:
                self.hover_pos = None
        else:
            self.hover_pos = None

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

                if self.hover_pos == (col, row):
                    pygame.draw.rect(surface, (255, 255, 255),
                                     pygame.Rect(x - 1, y - 1, self.tile_size + 2, self.tile_size + 2), 1)

    def get_plant_at(self, col, row):
        plants_in_row = self.context.layers["plants"].get(row, [])
        for plant in plants_in_row:
            if plant.col == col:
                return plant
        return None
