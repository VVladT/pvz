import sys
import pygame

from app.core.constants import SCALE_FACTOR, DATA
from app.core.wave_manager import WaveManager
from app.entities.plants.plant_factory import PlantFactory
from app.scenes.background import Background
from app.scenes.scene import Scene
from app.ui.sun_indicator import SunIndicator


class LevelScene(Scene):
    def __init__(self, context, store, board):
        super().__init__(context)
        self.store = store
        self.board = board
        self.background = Background(context)
        self.sun_indicator = SunIndicator(context)
        self.wave_manager = WaveManager(self.context, board)
        self.hover_pos = None

    def on_enter(self):
        pygame.mixer.music.load("assets/music/loonboon.mp3")
        pygame.mixer.music.play(-1)

        self.context.layers["background"].append(self.background)
        self.context.layers["background"].append(self.board)
        self.context.layers["ui"].append(self.store)
        self.context.layers["ui"].append(self.sun_indicator)

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = (mouse_pos[0] / SCALE_FACTOR, mouse_pos[1] / SCALE_FACTOR)

        self.store.update_hover(scaled_mouse_pos)
        self.wave_manager.update(dt)

        if self.store.get_item():
            self.board.update_hover(scaled_mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.store.selected_index = None
                self.board.update_hover(None)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for sun in self.context.layers["items"][:]:
                    if sun.is_hovered():
                        value = sun.collect()
                        self.context.sun_manager.add_sun(value)

                self.store.update_select(scaled_mouse_pos)

                if self.store.get_item():
                    col = int((scaled_mouse_pos[0] - self.board.x) // self.board.tile_size)
                    row = int((scaled_mouse_pos[1] - self.board.y) // self.board.tile_size)

                    if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
                        existing_plant = self.board.get_plant_at(col, row)
                        if existing_plant is None:
                            name = self.store.get_item().name
                            plant_data = DATA["plants"][name]
                            new_plant = PlantFactory.create_plant(
                                PlantFactory,
                                name,
                                plant_data["type"],
                                self.context,
                                (col * self.board.tile_size + self.board.x, row * self.board.tile_size + self.board.y),
                                (col, row)
                            )
                            if row not in self.context.layers["plants"]:
                                self.context.layers["plants"][row] = []
                            self.context.layers["plants"][row].append(new_plant)
                            self.context.sun_manager.spend_sun(self.store.get_item().price)
                            self.store.selected_index = None
                            self.board.update_hover(scaled_mouse_pos)

        for projectile in self.context.layers["projectiles"][:]:
            for zombie in self.context.layers["enemies"][projectile.row][:]:
                distance = zombie.pos[0] - projectile.pos[0]

                if 5 > distance > -5:
                    zombie.receive_damage(projectile.damage)
                    projectile.is_alive = False
                    break

        for row_zombies in self.context.layers["enemies"].values():
            for zombie in row_zombies:
                if zombie.pos[0] <= self.board.x:
                    pygame.mixer.music.stop()
                    self.context.scene_manager.set_scene("game_over")
                    return

        for sun in self.context.layers["items"][:]:
            if sun.is_hovered():
                self.context.mouse.set_state("pointer")
                break