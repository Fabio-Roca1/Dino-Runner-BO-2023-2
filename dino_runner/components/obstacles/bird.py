import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image1, image2, x_pos):
        super().__init__(image1)
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = random.randint(200, 345)
        self.speed = 2
        self.index = 0

    def update(self, game_speed, player):
        self.rect.x -= self.speed * game_speed
        self.animate()

    def animate(self):
        self.index += 1
        if self.index % 20 == 0:
            if self.image == self.image1:
                self.image = self.image2
            else:
                self.image = self.image1
        self.rect = self.image.get_rect(topleft=self.rect.topleft)