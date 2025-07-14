class BaseEntity:
    def __init__(self, context, pos):
        self.context = context
        self.pos = pos
        self.is_alive = True

    def update(self, dt):
        pass

    def draw(self, surface):
        pass