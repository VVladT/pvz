import pygame.mixer

from app.core.constants import LEVELS, SPRITES, WINDOW_DIMENSION
from app.scenes.board import Board
from app.scenes.level_scene import LevelScene
from app.ui.store import Store, Item


class SceneManager:
    def __init__(self, context):
        self.context = context
        self.scenes = {}
        self.current_scene = None

    def add_level(self, level_name):
        store = Store(self.context)
        board = Board(self.context)
        for item in LEVELS[level_name]["store_items"]:
            store.add_item(Item(self.context.spritesheet, item["type"], item["price"], SPRITES["store_icons"][item["type"]]))
        store.create_slots()
        self.scenes[level_name] = LevelScene(self.context, store, board)

    def set_scene(self, scene_name):
        pygame.mixer.music.load("assets/music/loonboon.mp3")
        pygame.mixer.music.play(-1)
        self.current_scene = self.scenes[scene_name]
        self.current_scene.on_enter()

    def update(self):
        self.context.dt = self.context.clock.tick(60) / 1000
        if self.current_scene:
            self.current_scene.update(self.context.dt)

    def draw(self):
        self.context.surface.fill((41, 173, 255))

        for layer_name in ["background", "plants", "projectiles", "enemies", "ui"]:
            for element in self.context.layers[layer_name]:
                element.draw(self.context.surface)

        self.context.mouse.set_state("normal")
        self.context.mouse.draw(self.context.surface)

        # Escalar y mostrar
        scaled = pygame.transform.scale(self.context.surface, WINDOW_DIMENSION)
        self.context.screen.blit(scaled, (0, 0))
        pygame.display.flip()