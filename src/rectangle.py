from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
        self.check_if_can_create_rectangle(width, height)

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def get_area(self):
        return self.width * self.height

    @staticmethod
    def check_if_can_create_rectangle(width, height):
        if not (width > 0 and height > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {width}, {height}')
