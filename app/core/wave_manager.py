import random

from app.entities.zombie import Zombie


class WaveManager:
    def __init__(self, context, board):
        self.context = context
        self.board = board
        self.time_since_last_wave = 0
        self.wave_interval = 15
        self.current_wave = 0

    def update(self, dt):
        self.time_since_last_wave += dt

        if self.time_since_last_wave >= self.wave_interval:
            self.start_wave()
            self.time_since_last_wave = 0

    def start_wave(self):
        self.current_wave += 1
        num_zombies = 1 + self.current_wave

        for _ in range(num_zombies):
            row = random.randint(0, self.board.rows - 1)

            zombie = Zombie(self.context, "basic", row)
            self.context.layers["enemies"][row].append(zombie)
