from app.scenes.scene import Scene


import pygame
import sys
from app.scenes.scene import Scene
from app.ui.start_ui import StartUI


class StartScene(Scene):
    def __init__(self, context):
        super().__init__(context)
        self.context = context

    def on_enter(self):
        self.context.layers["ui"].append(StartUI(self.context))
        pygame.mixer.music.load("assets/music/grasswalk.mp3")
        pygame.mixer.music.play(-1)

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.context.scene_manager.set_scene("level_3")
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
