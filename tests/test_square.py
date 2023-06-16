import pytest
from src.square import Square


@pytest.mark.parametrize('side, expected_perimeter, expected_area',
                         [
                             (5, 20, 25),
                             (2, 8, 4),
                             (1, 4, 1),
                         ]
                         )
def test_square_creation_positive(side, expected_perimeter, expected_area):
    square = Square(side)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert square.get_area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side',
                         [
                             (0),
                             (-2),
                         ],
                         ids=[
                             'side is zero',
                             'side is negative'
                         ])
def test_square_creation_negative(side):
    with pytest.raises(ValueError):
        Square(side)


def test_two_square_areas_sum():
    expected_sum = 26
    square_1 = Square(5)
    square_2 = Square(1)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_square_areas_sum_negative(some_other_class):
    square_1 = Square(10)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
