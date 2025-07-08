import pygame

class Sprite:
    def __init__(self, pos_sprite, size, spritesheet, has_border=False, border_color=(0,0,0)):
        self.pos_sprite = pos_sprite
        self.size = size
        self.has_border = has_border
        self.border_color = border_color
        self.spritesheet = spritesheet

    def draw(self, surface, pos):
        pos_sprite = self.pos_sprite
        frame_rect = pygame.Rect(pos_sprite[0], pos_sprite[1], self.size[0], self.size[1])
        frame_image = self.spritesheet.subsurface(frame_rect).copy()

        if self.has_border:
            border_image = pygame.Surface(frame_image.get_size(), pygame.SRCALPHA)

            mask = pygame.mask.from_surface(frame_image)
            mask_surface = mask.to_surface(setcolor=self.border_color + (255,), unsetcolor=(0, 0, 0, 0))
            border_image.blit(mask_surface, (0, 0))

            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for ox, oy in offsets:
                surface.blit(border_image, (pos[0] + ox, pos[1] + oy))

        surface.blit(frame_image, pos)

