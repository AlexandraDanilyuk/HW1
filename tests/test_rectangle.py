import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('width, height, expected_perimeter, expected_area',
                         [
                             (5, 10, 30, 50),
                             (2, 3, 10, 6),
                             (5, 6, 22, 30),
                         ]
                         )
def test_rectangle_creation_positive(width, height, expected_perimeter, expected_area):
    rectangle = Rectangle(width, height)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('width, height,',
                         [
                             (0, 10),
                             (-2, 2),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative'
                         ])
def test_rectangle_creation_negative(width, height):
    with pytest.raises(ValueError):
        Rectangle(width, height, )


def test_two_rectangle_areas_sum():
    expected_sum = 56
    rectangle_1 = Rectangle(10, 5)
    rectangle_2 = Rectangle(2, 3)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_rectangle_areas_sum_negative(some_other_class):
    rectangle_1 = Rectangle(10, 8)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
