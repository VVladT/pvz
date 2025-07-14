import pygame

from app.core.constants import WINDOW_DIMENSION, VIRTUAL_DIMENSION, SPRITES
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

        # Mouse
        self.mouse = Mouse(SPRITES["mouse"], self.spritesheet)
        self.mouse.set_state("normal")
        pygame.mouse.set_visible(False)

        # Entidades
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
