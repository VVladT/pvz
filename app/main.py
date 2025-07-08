import pygame

from app.constants import WINDOW_DIMENSION, VIRTUAL_DIMENSION, SPRITES
from app.scenes.scene_manager import SceneManager
from app.ui.mouse import Mouse
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

mouse = Mouse(SPRITES["mouse"], SPRITESHEET)
mouse.set_state("normal")
pygame.mouse.set_visible(False)

while running:
    dt = clock.tick(60) / 1000

    surface.fill((41,173,255))

    scene_manager.update(dt)
    scene_manager.draw(surface)
    mouse.draw(surface)

    scaled_surface = pygame.transform.scale(surface, WINDOW_DIMENSION)
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()

pygame.quit()