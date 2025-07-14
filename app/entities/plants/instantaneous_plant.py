from app.core.constants import DATA
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite


class InstantaneousPlant(Plant):
    def __init__(self, name, context, pos, pos_in_board):
        data = DATA["plants"][name]
        super(InstantaneousPlant, self).__init__(data, context, pos, 99999, pos_in_board)
        self.type = "instantaneous"
        self.sprites = []
        self.sprite_index = 0
        self.timer = 0
        self.delay = 0.5

        for i, frames in enumerate(data["frames"]):
            self.sprites.append(Sprite(data["frames"][i], data["size"], context.spritesheet, has_border=True))

    def update(self, dt):
        self.timer += dt

        if self.timer >= self.delay:
            self.timer = 0
            self.sprite_index += 1
            if self.sprite_index >= len(self.sprites):
                self.is_alive = False

        super().update(dt)

    def draw(self, surface):
        self.sprite = self.sprites[self.sprite_index]
        super().draw(surface)
