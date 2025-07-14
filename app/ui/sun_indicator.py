import pygame

from app.core.constants import DATA, VIRTUAL_DIMENSION
from app.entities.sprite import Sprite


class SunIndicator:
    def __init__(self, context):
        self.context = context
        data = DATA["sun"]
        self.sun_icon = Sprite(data["frames"][0], data["size"], context.spritesheet)
        self.suns = context.sun_manager.total
        self.font = pygame.font.Font("assets/fonts/main.ttf", 16)
        self.pos = (1, VIRTUAL_DIMENSION[1] - 12)
        self.size = (34,10)

    def draw(self, surface):
        x, y = self.pos
        width, height = self.size

        shadow_rect = pygame.Rect(x, y + 1, width, height)
        pygame.draw.rect(surface, (40, 40, 40), shadow_rect, border_radius=3)

        main_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, (171, 82, 54), main_rect, border_radius=3)

        icon_x = x + 1
        icon_y = y + (height - self.sun_icon.size[1]) // 2
        self.sun_icon.draw(surface, (icon_x, icon_y))

        counter_width = 22
        counter_height = height-2
        counter_x = x + self.sun_icon.size[0] + 2
        counter_y = y + 1
        counter_rect = pygame.Rect(counter_x, counter_y, counter_width, counter_height)

        pygame.draw.rect(surface, (255, 204, 170), counter_rect, border_radius=2)

        sun_total = self.context.sun_manager.total
        text = self.font.render(str(sun_total), True, (29, 43, 83))
        text_x = counter_x + 2
        text_y = counter_y - text.get_height() // 2 + 2
        surface.blit(text, (text_x, text_y))