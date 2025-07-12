import sys

import pygame

from app.core.constants import SCALE_FACTOR, SPRITES
from app.entities.plants.plant_factory import PlantFactory
from app.scenes.scene import Scene


class LevelScene(Scene):
    def __init__(self, spritesheet, store, board):
        super().__init__(spritesheet)
        self.store = store
        self.board = board
        self.hover_pos = None

    def on_enter(self):
        pass

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = (mouse_pos[0] / SCALE_FACTOR, mouse_pos[1] / SCALE_FACTOR)

        self.store.update_hover(scaled_mouse_pos)

        if self.store.get_item():
            self.board.update_hover(scaled_mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.store.selected_index = None
                self.board.update_hover(None)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.store.update_select(scaled_mouse_pos)

                if self.store.get_item():
                    col = int(scaled_mouse_pos[0] - self.board.x) // self.board.tile_size
                    row = int(scaled_mouse_pos[1] - self.board.y) // self.board.tile_size

                    if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
                        if self.board.grid[row][col] is None:
                            name = self.store.get_item().name
                            plant_data = SPRITES["plants"][name]
                            self.board.grid[row][col] = PlantFactory.create_plant(PlantFactory, name, plant_data["type"], self.spritesheet)
                            self.store.selected_index = None
        self.board.update_plants(dt)

    def draw(self, surface):
        self.store.draw(surface)
        self.board.draw(surface)
