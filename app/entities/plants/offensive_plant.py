from app.core.constants import SPRITES
from app.entities.plants.plant import Plant
from app.entities.projectile import Projectile
from app.entities.sprite import Sprite


class OffensivePlant(Plant):
    def __init__(self, name, spritesheet):
        data = SPRITES["plants"][name]
        super(OffensivePlant, self).__init__(data, spritesheet)
        self.type = "offensive"
        shooting_data = data["shooting"]
        self.state = "idle"
        self.shooting = Sprite(shooting_data["frames"][0], shooting_data["size"], spritesheet, has_border=True)
        idle_data = data["idle"]
        self.spritesheet = spritesheet
        self.idle_sprites = []
        self.idle_index = 0
        self.projectile_name = data["projectile"]
        self.projectiles = []

        for i, frames in enumerate(idle_data["frames"]):
            self.idle_sprites.append(Sprite(idle_data["frames"][i], idle_data["size"], spritesheet, has_border=True))

    def shoot(self, pos):
        self.projectiles.append(Projectile(self.projectile_name, self.spritesheet, pos))

    def update_state(self, state, dt):
        self.state = state

        for projectile in self.projectiles:
            projectile.update(dt)

        if self.state == "idle":
            self.idle_index += 1
            if self.idle_index >= len(self.idle_sprites):
                self.idle_index = 0

    def draw(self, surface, pos):
        if self.state == "idle":
            self.idle_sprites[self.idle_index].draw(surface, pos)

        if self.state == "shooting":
            self.shooting.draw(surface, pos)

        for projectile in self.projectiles:
            projectile.draw(surface)