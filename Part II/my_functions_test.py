
import pytest

# import mimesis

from my_functions import *

########################################
########################################
########################################

def test_is_palindrome():
    assert is_palindrome('Abdbt') == False
    assert is_palindrome('asdf4fdsa') == True
    assert is_palindrome('asdffdsa') == True
    assert is_palindrome('WWW') == True
    assert is_palindrome('WW') == True
    assert is_palindrome('W') == True
    assert is_palindrome('') == True





########################################

# Try to use @pytest.mark.parametrize #

test_data_multiplication = [
    (2, 2, 4),
    (2, 3, 6),
    (0, 8, 0),
]

@pytest.mark.parametrize("x, y, expected", test_data_multiplication)

def test_multiplication(x,y,expected):
    assert multiplication(x, y) == expected

########################################
########################################
########################################

if __name__ == "__main__":
    pytest.main(["-v","--no-header",__file__])
