
import pytest

# import mimesis

from my_functions import *

########################################

test_data_multiplication = [
    (2, 2, 4),
    (2, 3, 6),
    (0, 8, 0),
]

@pytest.mark.parametrize("x, y, expected", test_data_multiplication)

def test_multiplication(x,y,expected):
    assert multiplication(x, y) == expected

########################################

if __name__ == "__main__":
    pytest.main(["-v","--no-header",__file__])
