import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hummer import Hummer


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def generate_shield(self, score):
        self.generate_power_up(score, 300, 400, Shield)
        
    def generate_hummer(self,score):
        self.generate_power_up(score, 600, 900, Hummer)

    def generate_power_up(self, score, x, y, type):
        if len(self.power_ups) == 0 and self.when_appers == score:
            self.when_appers += random.randint(x, y)
            self.power_ups.append(type())

    def update(self, score, game_speed, player):
        self.generate_shield(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups =[]
        self.when_appers = random.randint(200, 300)   