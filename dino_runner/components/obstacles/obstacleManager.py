import pygame
import random

from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, HEART_TYPE, BACK_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.death_count += 1
                    pygame.time.delay(500)
                    game.playing = False
                    break
                else:
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE:
                        continue
                    elif game.player.type == HEART_TYPE:
                        game.game_speed += 5
                        self.obstacles.remove(obstacle)
                    elif game.player.type == BACK_TYPE:
                        game.game_speed = 20
                        continue
                        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []