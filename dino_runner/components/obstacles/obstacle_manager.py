import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import (
    SMALL_CACTUS, 
    LARGE_CACTUS
    )
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
           match random.randint(0, 2):
            case 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            case 1:
                self.obstacles.append(Bird(BIRD))
            case 2:
                self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
               if not game.player.shield:	

                    pygame.time.delay(300)
                    game.playing = False
                    break
               else:
                   self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)