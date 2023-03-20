import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus, Cactus_large


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0,1)
            if random_obstacle == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))  # adiciona algo na lista
            elif random_obstacle == 1:
                self.obstacles.append(Cactus_large(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)