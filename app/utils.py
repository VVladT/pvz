import pygame

def load_image(path, colorkey=None):
    image = pygame.image.load(path).convert()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    return image
