import pygame.mixer

from app.constants import LEVELS, SPRITES
from app.scenes.board import Board
from app.scenes.level_scene import LevelScene
from app.ui.store import Store, Item


class SceneManager:
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet
        self.scenes = {}
        self.current_scene = None

    def add_level(self, level_name):
        store = Store(self.spritesheet)
        board = Board(self.spritesheet)
        for item in LEVELS[level_name]["store_items"]:
            store.add_item(Item(self.spritesheet, item["type"], item["price"], SPRITES["store_icons"][item["type"]]))
        store.create_slots()
        self.scenes[level_name] = LevelScene(self.spritesheet, store, board)

    def set_scene(self, scene_name):
        pygame.mixer.music.load("assets/music/grasswalk.mp3")
        pygame.mixer.music.play(-1)
        self.current_scene = self.scenes[scene_name]
        self.current_scene.on_enter()

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def draw(self, surface):
        if self.current_scene:
            self.current_scene.draw(surface)