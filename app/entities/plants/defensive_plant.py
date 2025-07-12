from app.core.constants import SPRITES
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite


class DefensivePlant(Plant):
    def __init__(self, name, spritesheet):
        data = SPRITES["plants"][name]
        super(DefensivePlant, self).__init__(data, spritesheet)
        self.type = "defensive"
        self.state = "full"
        self.states = {
            "full": Sprite(data["full"]["frames"][0], data["full"]["size"], spritesheet, has_border=True),
            "damaged": Sprite(data["damaged"]["frames"][0], data["damaged"]["size"], spritesheet, has_border=True),
            "critical": Sprite(data["critical"]["frames"][0], data["critical"]["size"], spritesheet, has_border=True),
        }


    def update_state(self, state):
        self.state = state

    def draw(self, surface, pos):
        self.states[self.state].draw(surface, pos)
