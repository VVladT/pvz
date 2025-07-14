from app.core.constants import DATA
from app.entities.plants.plant import Plant
from app.entities.projectile import Projectile
from app.entities.sprite import Sprite


class OffensivePlant(Plant):
    def __init__(self, name, context, pos, pos_in_board, idle_delay = 0.4):
        data = DATA["plants"][name]
        super().__init__(data, context, pos, data["hp"], pos_in_board)
        self.type = "offensive"
        shooting_data = data["shooting"]
        spritesheet = context.spritesheet
        self.state = "idle"
        self.shooting = Sprite(shooting_data["frames"][0], shooting_data["size"], spritesheet, has_border=True)
        idle_data = data["idle"]
        self.idle_sprites = []
        self.idle_index = 0
        self.projectile_name = data["projectile"]
        self.atack_delay = data["atack_delay"]
        self.num_atacks = data["num_atacks"]
        self.idle_delay = idle_delay
        self.atack_timer = 0
        self.idle_timer = 0

        for i, frames in enumerate(idle_data["frames"]):
            self.idle_sprites.append(Sprite(idle_data["frames"][i], idle_data["size"], spritesheet, has_border=True))

    def update(self, dt):
        self.atack_timer += dt
        self.idle_timer += dt

        if self._has_enemy_in_front():
            if self.atack_timer >= self.atack_delay:
                self.atack_timer = 0
                self._shoot()

        if self.atack_timer >= self.idle_delay:
            self.state = "idle"

        if self.state == "idle" and self.idle_timer >= self.idle_delay:
            self.idle_timer = 0
            self.idle_index += 1
            if self.idle_index >= len(self.idle_sprites):
                self.idle_index = 0

        super().update(dt)

    def draw(self, surface):
        if self.state == "idle":
            self.sprite = self.idle_sprites[self.idle_index]

        if self.state == "shooting":
            self.sprite = self.shooting

        super().draw(surface)

    def _shoot(self):
        self.state = "shooting"

        for _ in range(self.num_atacks):
            x = self.pos[0] + 5
            y = self.pos[1] + 1
            projectile = Projectile(self.projectile_name, self.context, [x, y], self.row)
            self.context.layers["projectiles"].append(projectile)

    def _has_enemy_in_front(self):
        for zombie in self.context.layers["enemies"][self.row]:
            if zombie.pos[0] > self.pos[0]:
                return True
        return False