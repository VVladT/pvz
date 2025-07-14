import sys

import pygame

from app.core.game_context import GameContext
from app.scenes.scene_manager import SceneManager


def main():
    pygame.init()
    context = GameContext()
    scene_manager = SceneManager(context)
    scene_manager.add_level("level_3")
    scene_manager.set_scene("level_3")

    while True:
        scene_manager.update()
        scene_manager.draw()

if __name__ == "__main__":
    main()