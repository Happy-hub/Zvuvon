import math


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
