import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hummer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.back import Back


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def generate_power_up(self, score):
        power_up_type = [Shield(), Hammer(), Heart(), Back()]

        if len(self.power_ups) == 0 and self.when_appers == score:
            self.when_appers += random.randint(200, 400)
            self.power_ups.append(power_up_type[random.randint(0, 3)])

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups =[]
        self.when_appers = random.randint(200, 400)   