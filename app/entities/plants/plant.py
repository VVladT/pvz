from app.entities.entity import BaseEntity


class Plant(BaseEntity):
    def __init__(self, data, context, pos, hp, pos_in_board):
        super().__init__(context, pos)
        self.data = data
        self.hp = hp
        self.type = None
        self.row = pos_in_board[1]
        self.col = pos_in_board[0]
        self.was_damaged = False
        self.damage_flash_timer = 0
        self.flash_duration = 0.15
        self.sprite = None

    def update(self, dt):
        if self.hp <= 0:
            self.is_alive = False

        if self.was_damaged:
            self.damage_flash_timer -= dt
            if self.damage_flash_timer <= 0:
                self.was_damaged = False

    def draw(self, surface):
        if self.was_damaged:
            self.sprite.has_border = True
            self.sprite.border_color = (255, 255, 255)
        else:
            self.sprite.border_color = (0, 0, 0)

        self.sprite.draw(surface, self.pos)

    def receive_damage(self, amount):
        if self.is_alive:
            self.hp -= amount
            self.was_damaged = True
            self.damage_flash_timer = self.flash_duration
