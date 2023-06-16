from src.figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
        self.check_if_can_create_square(side)

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def get_area(self):
        return self.side ** 2

    @staticmethod
    def check_if_can_create_square(side):
        if not (side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {side}')
