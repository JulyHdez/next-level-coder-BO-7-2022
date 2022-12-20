import random
from dino_runner.utils.constants import CLOUD

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.image_width = self.image.get_width()
        self.x_pos_cloud = random.randint(800,1000)
        self.y_pos_cloud = random.randint(50,100)
        self.game_speed = 50
    
    def update(self):
        self.x_pos_cloud = self.game_speed
        if self.x_pos_cloud <= -self.image_width:
            self.x_pos_cloud = self.image_width + random.randint(2500,3000)
            self.y_pos_cloud = random.randint(50,100) 

    def draw(self, screen):
       screen.blit(self.image,(self.x_pos_cloud,self.y_pos_cloud))