import pygame

from app.core.game_context import GameContext


def main():
    pygame.init()
    context = GameContext()

    while True:
        context.update()
        context.draw()

if __name__ == "__main__":
    main()