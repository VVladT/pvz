from app.core.constants import SPRITES
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite


class SunProducerPlant(Plant):
    def __init__(self, name, spritesheet):
        data = SPRITES["plants"][name]
        super(SunProducerPlant, self).__init__(data, spritesheet)
        self.type = "sun_producer"
        producing_data = data["producing"]
        self.state = "idle"
        self.producing = Sprite(producing_data["frames"][0], producing_data["size"], spritesheet, has_border=True)
        idle_data = data["idle"]
        self.idle_sprites = []
        self.idle_index = 0

        for i, frames in enumerate(idle_data["frames"]):
            self.idle_sprites.append(Sprite(idle_data["frames"][i], idle_data["size"], spritesheet, has_border=True))

    def update_state(self, state):
        self.state = state

        if self.state == "idle":
            self.idle_index += 1
            if self.idle_index >= len(self.idle_sprites):
                self.idle_index = 0

    def draw(self, surface, pos):
        if self.state == "idle":
            self.idle_sprites[self.idle_index].draw(surface, pos)

        if self.state == "producing":
            self.producing.draw(surface, pos)
