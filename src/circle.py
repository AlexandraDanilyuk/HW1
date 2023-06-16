from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        self.check_if_can_create_circle(radius)

    @property
    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)

    @property
    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

    @staticmethod
    def check_if_can_create_circle(radius):
        if not (radius > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {radius}')
