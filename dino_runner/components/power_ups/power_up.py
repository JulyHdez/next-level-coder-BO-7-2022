from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.y = 125
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            power_ups.pop()


    def draw(self,screen):
        screen.blit(self.image, self.rect)