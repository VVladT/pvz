class Background:
    def __init__(self, context):
        self.context = context

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((41, 173, 255))