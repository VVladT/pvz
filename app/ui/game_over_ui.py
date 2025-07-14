import pygame
from app.core.constants import VIRTUAL_DIMENSION

class GameOverUI:
    def __init__(self, context):
        self.context = context
        self.font = pygame.font.Font("assets/fonts/main.ttf", 32)
        self.small_font = pygame.font.Font("assets/fonts/main.ttf", 16)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((20, 20, 20))

        center_x = VIRTUAL_DIMENSION[0] // 2

        # Render textos
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart = self.small_font.render("Presiona R para reiniciar", True, (255, 255, 255))
        quit_text = self.small_font.render("Presiona ESC para salir", True, (200, 200, 200))

        # Calcular posiciones centradas
        surface.blit(text, (center_x - text.get_width() // 2, 20))
        surface.blit(restart, (center_x - restart.get_width() // 2, 60))
        surface.blit(quit_text, (center_x - quit_text.get_width() // 2, 80))
