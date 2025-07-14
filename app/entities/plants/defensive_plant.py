from app.core.constants import DATA
from app.entities.plants.plant import Plant
from app.entities.sprite import Sprite


class DefensivePlant(Plant):
    def __init__(self, name, context, pos, pos_in_board):
        data = DATA["plants"][name]
        super(DefensivePlant, self).__init__(data, context, pos, data["hp"], pos_in_board)
        self.max_hp = self.hp
        self.type = "defensive"
        self.state = "full"
        self.states = {
            "full": Sprite(data["full"]["frames"][0], data["full"]["size"], context.spritesheet, has_border=True),
            "damaged": Sprite(data["damaged"]["frames"][0], data["damaged"]["size"], context.spritesheet, has_border=True),
            "critical": Sprite(data["critical"]["frames"][0], data["critical"]["size"], context.spritesheet, has_border=True),
        }
        self.base_eye_positions = [(pos[0] + 5, pos[1] + 4), (pos[0] + 9, pos[1] + 4)]
        self.eye_offsets = [0, 0]
        self.eye_move_timer = 0
        self.eye_move_delay = 1.2


    def update(self, dt):
        super().update(dt)

        self.eye_move_timer += dt
        if self.eye_move_timer >= self.eye_move_delay:
            self.eye_move_timer = 0
            self._move_eyes()

        if self.hp > self.max_hp * 0.5:
            self.state = "full"
        elif self.hp > self.max_hp * 0.2:
            self.state = "damaged"
        else:
            self.state = "critical"


    def draw(self, surface):
        self.sprite = self.states[self.state]
        super().draw(surface)

        for i, eye_position in enumerate(self.base_eye_positions):
            new_x = eye_position[0] + self.eye_offsets[i]
            surface.set_at((new_x, eye_position[1]), (0, 0, 0))

    def _move_eyes(self):
        self.eye_offsets[0] = -1 if self.eye_offsets[0] == 0 else 0
        self.eye_offsets[1] = -1 if self.eye_offsets[1] == 0 else 0