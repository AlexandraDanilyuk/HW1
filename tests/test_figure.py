import pytest
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


def test_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle"
    assert triangle.get_area == 6.0
    assert triangle.perimeter == 12


def test_rectangle():
    rectangle = Rectangle(5, 6)
    assert rectangle.name == "Rectangle"
    assert rectangle.get_area == 30
    assert rectangle.perimeter == 22


def test_square():
    square = Square(4)
    assert square.name == "Square"
    assert square.get_area == 16
    assert square.perimeter == 16


def test_circle():
    circle = Circle(3)
    assert circle.name == "Circle"
    assert circle.get_area == pytest.approx(28.27)
    assert circle.get_perimeter == pytest.approx(18.85)


def test_invalid_figure():
    rectangle = Rectangle(5, 6)
    invalid_figure = "InvalidFigure"

    with pytest.raises(ValueError):
        rectangle.add_area(invalid_figure)
