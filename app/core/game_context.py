import pygame

from app.core.constants import WINDOW_DIMENSION, VIRTUAL_DIMENSION, SPRITES
from app.scenes.board import Board
from app.scenes.scene_manager import SceneManager
from app.ui.mouse import Mouse
from app.utils import load_image


class GameContext:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_DIMENSION)
        self.surface = pygame.Surface(VIRTUAL_DIMENSION)
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Recursos
        self.spritesheet = load_image("assets/sprites/spritesheet.png", colorkey=(255, 119, 168))
        self.font = pygame.font.Font("assets/fonts/main.ttf", 16)

        # Escenas
        self.scene_manager = SceneManager(self)
        self.scene_manager.add_level("level_3")
        self.scene_manager.set_scene("level_3")

        # Mouse personalizado
        self.mouse = Mouse(SPRITES["mouse"], self.spritesheet)
        self.mouse.set_state("normal")
        pygame.mouse.set_visible(False)

        # Entidades
        self.board = Board(self.spritesheet)
        self.projectiles = []
        self.enemies = []

        # Capas visuales
        self.layers = {
            "background": [],
            "plants": [],
            "projectiles": [],
            "enemies": [],
            "ui": []
        }

    def update(self):
        self.dt = self.clock.tick(60) / 1000
        self.scene_manager.update(self.dt)

    def draw(self):
        self.surface.fill((41, 173, 255))
        self.mouse.set_state("normal")
        self.scene_manager.draw(self.surface)
        self.mouse.draw(self.surface)

        # Escalar y mostrar
        scaled = pygame.transform.scale(self.surface, WINDOW_DIMENSION)
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()
