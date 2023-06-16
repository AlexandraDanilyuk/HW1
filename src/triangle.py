from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.check_if_can_create_triangle(a, b, c)

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def get_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return round(area, 2)

    @staticmethod
    def check_if_can_create_triangle(a: int, b: int, c: int):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a}, {b}, {c}')

        if not (a + b > c and a + c > b and c + b > a):
            raise ValueError(f'Unable to create a triangle with sides: {a}, {b}, {c}')
