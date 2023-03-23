from dino_runner.utils.constants import BACK, BACK_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Back(PowerUp):
    def __init__(self):
        self.image = BACK
        self.type = BACK_TYPE
        super().__init__(self.image, self.type)