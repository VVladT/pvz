from app.constants import SPRITES
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite


class InstantaneousPlant(Plant):
    def __init__(self, name, spritesheet):
        data = SPRITES["plants"][name]
        super(InstantaneousPlant, self).__init__(data, spritesheet)
        self.type = "instantaneous"
        self.sprites = []
        self.sprite_index = 0

        for i, frames in enumerate(data["frames"]):
            self.sprites.append(Sprite(data["frames"][i], data["size"], spritesheet, has_border=True))

    def update_state(self):
        self.sprite_index += 1
        if self.sprite_index >= len(self.sprites):
            self.sprite_index = 0

    def draw(self, surface, pos):
        self.sprites[self.sprite_index].draw(surface, pos)
        #self.shooting.draw(surface, pos)

