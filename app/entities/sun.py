import math
import random
from app.core.constants import DATA
from app.entities.entity import BaseEntity
from app.entities.sprite import Sprite


class Sun(BaseEntity):
    def __init__(self, context, pos, value, arc_duration=0.6, fall_distance=7, lifetime=7.0):
        super().__init__(context, pos)
        data = DATA["sun"]
        self.value = value
        self.sprite = Sprite(data["frames"][0], data["size"], context.spritesheet)
        self.size = data["size"]

        self.start_x = pos[0]
        self.start_y = pos[1]
        self.x = self.start_x
        self.y = self.start_y

        self.arc_duration = arc_duration
        self.fall_distance = fall_distance
        self.arc_height = 5
        self.offset_x = random.choice([-3, -2, -1, 0, 1, 2, 3])
        self.state = "arc"
        self.timer = 0
        self.velocity_y = 40

        self.lifetime = lifetime
        self.idle_timer = 0

    def update(self, dt):
        self.timer += dt

        if self.state == "arc":
            t = min(self.timer / self.arc_duration, 1.0)
            self.x = self.start_x + self.offset_x * t
            self.y = self.start_y - self.arc_height * math.sin(t * math.pi)

            if t >= 1.0:
                self.state = "falling"
                self.start_fall_y = self.y
                self.timer = 0

        elif self.state == "falling":
            self.y += self.velocity_y * dt
            if self.y >= self.start_fall_y + self.fall_distance:
                self.y = self.start_fall_y + self.fall_distance
                self.state = "idle"
                self.idle_timer = 0

        elif self.state == "idle":
            self.idle_timer += dt
            if self.idle_timer >= self.lifetime:
                self.is_alive = False

    def draw(self, surface):
        self.sprite.draw(surface, (int(self.x), int(self.y)))

    def collect(self):
        self.is_alive = False
        return self.value

    def is_hovered(self):
        mx, my = self.context.mouse.get_scaled_pos()
        x, y = self.x, self.y
        w, h = self.size
        return x <= mx <= x + w and y <= my <= y + h
