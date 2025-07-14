from app.entities.entity import BaseEntity
from app.entities.sprite import Sprite
from app.core.constants import TILE_SIZE, DATA, VIRTUAL_DIMENSION


class Zombie(BaseEntity):
    def __init__(self, context, name, row):
        self.context = context
        self.name = name
        self.data = DATA["zombies"][name]
        self.size = DATA["zombies"][name]["walking"]["size"]

        self.was_damaged = False
        self.damage_flash_timer = 0
        self.flash_duration = 0.15

        self.hp = self.data["hp"]
        self.speed = self.data["speed"]
        self.damage = self.data["damage"]

        self.state = "walking"
        self.timer = 0
        self.anim_index = 0
        self.anim_delay = 0.3

        self.eating_delay = 0.5
        self.eating_timer = 0

        self.death_duration = 1.5
        self.dead_timer = 0

        x = VIRTUAL_DIMENSION[0]
        y = row * TILE_SIZE + 32
        self.row = row
        super().__init__(context, [x, y])

        self.target_plant = None

        # Cargar sprites
        self.animations = {}
        for key in ["walking", "eating", "dying", "dead"]:
            frames = self.data[key]["frames"]
            size = self.data[key]["size"]
            self.animations[key] = [
                Sprite(frame, size, context.spritesheet, has_border=True) for frame in frames
            ]

    def update(self, dt):
        self.timer += dt

        if self.was_damaged:
            self.damage_flash_timer -= dt
            if self.damage_flash_timer <= 0:
                self.was_damaged = False

        if self.hp <= 0 and self.state not in ["dying", "dead"]:
            self.state = "dying"
            self.timer = 0
            self.anim_index = 0

        if self.state == "dead":
            self.dead_timer += dt
            if self.dead_timer > self.death_duration:
                self.is_alive = False
            return

        if self.state == "dying":
            if self.anim_index >= len(self.animations["dying"]):
                self.anim_index = len(self.animations["dying"]) - 1
            if self.timer > 0.8:
                self.state = "dead"
                self.dead_timer = 0
            return

        if self.state == "walking":
            self.pos[0] -= self.speed * dt
            self._check_for_plants()

        elif self.state == "eating":
            if self.target_plant:
                self._damage_plant(dt)
            else:
                self.state = "walking"
                self.anim_index = 0

        if self.timer >= self.anim_delay:
            self.timer = 0
            self.anim_index += 1

            max_index = len(self.animations[self.state])
            if self.anim_index >= max_index:
                self.anim_index = 0

    def draw(self, surface):
        sprite = self.animations[self.state][self.anim_index]

        sprite_width, sprite_height = sprite.size

        draw_x = int(self.pos[0])
        draw_y = int(self.pos[1] + TILE_SIZE - sprite_height)

        if self.was_damaged:
            sprite.has_border = True
            sprite.border_color = (255, 255, 255)
        else:
            sprite.border_color = (0, 0, 0)

        sprite.draw(surface, (draw_x, draw_y))

    def receive_damage(self, amount):
        if self.state in ["dying", "dead"]:
            return

        self.hp -= amount
        self.was_damaged = True
        self.damage_flash_timer = self.flash_duration
        if self.hp <= 0:
            self.state = "dying"
            self.anim_index = 0
            self.timer = 0

    def _check_for_plants(self):
        plants_in_row = self.context.layers["plants"].get(self.row, [])

        for plant in plants_in_row:
            plant_x = plant.pos[0]
            zombie_x = self.pos[0]

            if zombie_x < plant_x + TILE_SIZE and zombie_x + TILE_SIZE > plant_x:
                self.state = "eating"
                self.target_plant = plant
                self.anim_index = 0
                self.timer = 0
                self.eating_timer = 0
                return

    def _damage_plant(self, dt):
        self.eating_timer += dt
        if self.eating_timer >= self.eating_delay:
            if self.target_plant:
                self.target_plant.receive_damage(self.damage)
                self.eating_timer = 0
                if not self.target_plant.is_alive:
                    self.target_plant = None
                    self.state = "walking"
                    self.anim_index = 0
                    self.timer = 0
