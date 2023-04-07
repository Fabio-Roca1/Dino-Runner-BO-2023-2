import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    Y_POS_CACTUS_SMALL = 325
    Y_POS_CACTUS_LARGE = 300

    def __init__(self, height):
        self.type = random.randint(0, 2)
        if height == "small":
            image = SMALL_CACTUS[self.type]
            y_pos = 325
        else:
            image = LARGE_CACTUS[self.type]
            y_pos = 300
        super().__init__(image)
        self.rect.y = y_pos
        