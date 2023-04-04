from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.step_index = 0

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus("small"))
            self.obstacles.append(Cactus("large"))
            self.obstacles.append(Bird(BIRD[0], BIRD[1], SCREEN_WIDTH))
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)