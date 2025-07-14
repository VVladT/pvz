import pygame

from app.core.constants import SCALE_FACTOR
from app.entities.sprite import Sprite


class Mouse:
    def __init__(self, sprite_data, spritesheet):
        self.states = {}
        self.current_state = "normal"
        self.spritesheet = spritesheet

        for state, data in sprite_data.items():
            frame_pos = data["frames"][0]
            size = data["size"]
            self.states[state] = Sprite(frame_pos, size, spritesheet)

    def set_state(self, state_name):
        if state_name in self.states:
            self.current_state = state_name

    def get_scaled_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] / SCALE_FACTOR, mouse_pos[1] / SCALE_FACTOR

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = (mouse_pos[0] / SCALE_FACTOR, mouse_pos[1] / SCALE_FACTOR)
        sprite = self.states[self.current_state]
        sprite.draw(surface, scaled_mouse_pos)