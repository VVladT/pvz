import pygame

from app.core.constants import WINDOW_DIMENSION, VIRTUAL_DIMENSION, DATA
from app.core.sun_manager import SunManager
from app.ui.mouse import Mouse
from app.utils import load_image


class GameContext:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_DIMENSION, pygame.NOFRAME)
        self.surface = pygame.Surface(VIRTUAL_DIMENSION)
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Recursos
        self.spritesheet = load_image("assets/sprites/spritesheet.png", colorkey=(255, 119, 168))
        self.font = pygame.font.Font("assets/fonts/main.ttf", 16)

        # Managers
        self.sun_manager = SunManager()
        self.scene_manager = None

        # Mouse
        self.mouse = Mouse(DATA["mouse"], self.spritesheet)
        self.mouse.set_state("normal")
        pygame.mouse.set_visible(False)

        # Entidades
        self.projectiles = []
        self.enemies = []

        # Capas visuales
        self.layers = {
            "background": [],
            "plants": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: []
            },
            "projectiles": [],
            "enemies": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: []
            },
            "items": [],
            "ui": []
        }

    def reset_layers(self):
        self.layers = {
            "background": [],
            "plants": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: []
            },
            "projectiles": [],
            "enemies": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: []
            },
            "items": [],
            "ui": []
        }