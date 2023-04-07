from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMMER_TYPE

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMMER_TYPE
        super().__init__(self.image, self.type)  
        

