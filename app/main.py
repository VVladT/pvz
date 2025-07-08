import pygame

from app.constants import WINDOW_DIMENSION, VIRTUAL_DIMENSION, SCALE_FACTOR
from app.scenes.scene_manager import SceneManager
from utils import load_image

pygame.init()
screen = pygame.display.set_mode(WINDOW_DIMENSION)
surface = pygame.Surface(VIRTUAL_DIMENSION)
clock = pygame.time.Clock()

SPRITESHEET = load_image("assets/sprites/spritesheet.png", colorkey=(255, 119, 168))

running = True
scene_manager = SceneManager(SPRITESHEET)
scene_manager.add_level("level_3")
scene_manager.set_scene("level_3")

while running:
    dt = clock.tick(60) / 1000
    mouse_pos = pygame.mouse.get_pos()
    scaled_mouse_pos = (mouse_pos[0] / SCALE_FACTOR, mouse_pos[1] / SCALE_FACTOR)

    surface.fill((41,173,255))

    scene_manager.update(dt)
    scene_manager.draw(surface)

    scaled_surface = pygame.transform.scale(surface, WINDOW_DIMENSION)
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()

pygame.quit()