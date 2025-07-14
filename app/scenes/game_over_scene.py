import sys

import pygame

from app.scenes.scene import Scene
from app.ui.game_over_ui import GameOverUI


class GameOverScene(Scene):
    def __init__(self, context):
        super().__init__(context)
        self.context = context

    def on_enter(self):
        pygame.mixer.music.load("assets/music/grasswalk.mp3")
        pygame.mixer.music.play(-1)
        self.context.layers["ui"].append(GameOverUI(self.context))

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.context.scene_manager.set_scene("level_3")
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
