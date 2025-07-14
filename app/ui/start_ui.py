import pygame
from app.core.constants import VIRTUAL_DIMENSION

class StartUI:
    def __init__(self, context):
        self.context = context
        self.font = pygame.font.Font("assets/fonts/main.ttf", 32)
        self.small_font = pygame.font.Font("assets/fonts/main.ttf", 16)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((20, 20, 20))

        center_x = VIRTUAL_DIMENSION[0] // 2
        center_y = VIRTUAL_DIMENSION[1] // 2

        # Lista de líneas de texto
        text_lines = ["Plants", "VS", "Zombies", "mini"]

        total_text_height = len(text_lines) * self.font.get_height() - 15
        start_y = center_y - total_text_height // 2 - 20

        # Dibujar cada línea de texto
        for i, line in enumerate(text_lines):
            text = self.font.render(line, True, (0, 255, 0))
            surface.blit(text, (center_x - text.get_width() // 2,
                                start_y + i * (self.font.get_height() - 10)))

        # Texto para reiniciar y salir (debajo del título)
        start = self.small_font.render("Presiona ENTER para jugar", True, (255, 255, 255))
        quit_text = self.small_font.render("Presiona ESC para salir", True, (200, 200, 200))

        # Posicionar el texto de reiniciar y salir en la parte inferior
        surface.blit(start, (center_x - start.get_width() // 2,
                               start_y + total_text_height))
        surface.blit(quit_text, (center_x - quit_text.get_width() // 2,
                                 start_y + total_text_height + 20))
