import pygame

from app.core.constants import DATA
from app.entities.entity import BaseEntity
from app.entities.sprite import Sprite


class Projectile(BaseEntity):
    def __init__(self, name, context, pos, row):
        super().__init__(context, pos)
        data = DATA["projectiles"][name]
        self.sprite = Sprite(data["frames"][0], data["size"], context.spritesheet, has_border=True)
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], data["size"][0], data["size"][1])
        self.damage = data["damage"]
        self.row = row

    def update(self, dt):
        self.pos[0] += 100 * dt

    def draw(self, surface):
        self.sprite.draw(surface, self.pos)