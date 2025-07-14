from app.core.constants import DATA
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite
from app.entities.sun import Sun


class SunProducerPlant(Plant):
    def __init__(self, name, context, pos, pos_in_board, idle_delay=0.4):
        data = DATA["plants"][name]
        super().__init__(data, context, pos, data["hp"], pos_in_board)
        spritesheet = context.spritesheet

        self.type = "sun_producer"
        self.state = "idle"

        self.sun_value = data["sun_value"]
        self.produce_delay = data["produce_delay"]
        self.produce_timer = 0
        self.idle_delay = idle_delay
        self.idle_timer = 0

        self.idle_sprites = []
        self.idle_index = 0

        # Sprites
        idle_data = data["idle"]
        for frame in idle_data["frames"]:
            self.idle_sprites.append(Sprite(frame, idle_data["size"], spritesheet, has_border=True))

        producing_data = data["producing"]
        self.producing = Sprite(producing_data["frames"][0], producing_data["size"], spritesheet, has_border=True)

    def update(self, dt):
        self.produce_timer += dt
        self.idle_timer += dt

        if self.produce_timer >= self.produce_delay:
            self.produce_timer = 0
            self.state = "producing"
            self._produce_sun()

        if self.produce_timer >= self.idle_delay:
            self.state = "idle"

        if self.state == "idle" and self.idle_timer >= self.idle_delay:
            self.idle_timer = 0
            self.idle_index = (self.idle_index + 1) % len(self.idle_sprites)
            
        super().update(dt)

    def _produce_sun(self):
        x = self.pos[0]
        y = self.pos[1]
        sun = Sun(self.context, (x, y), self.sun_value)
        self.context.layers["items"].append(sun)

    def draw(self, surface):
        if self.state == "idle":
            self.sprite = self.idle_sprites[self.idle_index]
        elif self.state == "producing":
            self.sprite = self.producing
        
        super().draw(surface)