from app.core.constants import SPRITES
from app.entities.sprite import Sprite


class Projectile:
    def __init__(self, name, spritesheet, pos):
        data = SPRITES["projectiles"][name]
        self.sprite = Sprite(data["frames"][0], data["size"], spritesheet, has_border=True)
        self.pos = pos

    def update(self, dt):
        self.pos[0] += 0.1 // dt

    def draw(self, surface):
        self.sprite.draw(surface, self.pos)