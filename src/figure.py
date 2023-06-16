class Figure:
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument should be a geometric figure.")

        return round(self.get_area + figure.get_area, 2)
