import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.power_up_counter = 0
        
    def update(self, game_speed, points, player):
        if points >= 100 and self.power_up_counter == 0:
            if random.choice([True, False]):
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())
            self.power_up_counter = 1
        
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)
            
        if self.power_up_counter > 0:
            self.power_up_counter += 1
            if self.power_up_counter > 200:
                self.power_up_counter = 0
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)