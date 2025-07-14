import pygame.mixer

from app.core.constants import LEVELS, DATA, WINDOW_DIMENSION, VIRTUAL_DIMENSION
from app.scenes.board import Board
from app.scenes.game_over_scene import GameOverScene
from app.scenes.level_scene import LevelScene
from app.scenes.start_scene import StartScene
from app.ui.store import Store, Item


class SceneManager:
    def __init__(self, context):
        self.context = context
        self.context.scene_manager = self
        self.scenes = {}
        self.current_scene = None
        self.scenes["start"] = StartScene(context)
        self.scenes["game_over"] = GameOverScene(context)

    def add_level(self, level_name):
        store = Store(self.context)
        board = Board(self.context)

        for item in LEVELS[level_name]["store_items"]:
            store.add_item(Item(self.context, item["type"], item["price"], DATA["store_icons"][item["type"]]))
        store.create_slots()
        self.scenes[level_name] = LevelScene(self.context, store, board)

    def set_scene(self, scene_name):
        self.context.reset_layers()
        self.current_scene = self.scenes[scene_name]
        self.current_scene.on_enter()

    def update(self):
        self.context.mouse.set_state("normal")
        self.context.dt = self.context.clock.tick(60) / 1000
        if self.current_scene:
            self.current_scene.update(self.context.dt)

        for layer_name in ["background", "plants", "projectiles", "enemies", "items", "ui"]:
            layer = self.context.layers[layer_name]

            if layer_name in ["plants", "enemies"]:
                for row_entities in layer.values():
                    for element in row_entities[:]:
                        if hasattr(element, "update"):
                            element.update(self.context.dt)

                        if hasattr(element, "pos"):
                            if element.pos[0] > VIRTUAL_DIMENSION[0] + 30 or element.pos[1] > VIRTUAL_DIMENSION[1] + 30:
                                row_entities.remove(element)

                        if hasattr(element, "is_alive") and not element.is_alive:
                            row_entities.remove(element)

            else:
                for element in layer[:]:
                    if hasattr(element, "update"):
                        element.update(self.context.dt)

                    if hasattr(element, "pos"):
                        if element.pos[0] > VIRTUAL_DIMENSION[0] + 30 or element.pos[1] > VIRTUAL_DIMENSION[1] + 30:
                            layer.remove(element)

                    if hasattr(element, "is_alive") and not element.is_alive:
                        layer.remove(element)

    def draw(self):
        for layer_name in ["background", "plants", "projectiles", "enemies", "items", "ui"]:
            layer = self.context.layers[layer_name]

            if layer_name in ["plants", "enemies"]:
                for row_entities in layer.values():
                    for element in row_entities:
                        if hasattr(element, "draw"):
                            element.draw(self.context.surface)
            else:
                for element in layer:
                    if hasattr(element, "draw"):
                        element.draw(self.context.surface)

        self.context.mouse.draw(self.context.surface)

        scaled = pygame.transform.scale(self.context.surface, WINDOW_DIMENSION)
        self.context.screen.blit(scaled, (0, 0))
        pygame.display.flip()