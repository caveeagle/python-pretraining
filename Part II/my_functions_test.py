
import pytest
import mimesis

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



def test_reverse_string():
    assert reverse_string('asfrt') == 'trfsa'

def test_is_divisible():
    assert is_divisible(30,10) == True  
    assert is_divisible(31,20) == False  
    assert is_divisible(0,20)  == True  
    
    # Check raises ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        is_divisible(88,0)  # must be TypeError

def test_longest_word():

    text = mimesis.Text(seed=143)  
    words_list = [text.word() for _ in range(10)]  
    
    longer_than_longest_word = longest_word(words_list)+'_'+words_list[0]
    words_list.append(longer_than_longest_word)
    
    
    print('\n'*3)
    print(words_list)
    print('The longest word is:',longest_word(words_list))
    print('\n'*3)

    assert longest_word(words_list) == longer_than_longest_word


def test_sum_of_digits():
    
    assert sum_of_digits(452) == 11
    assert sum_of_digits(4520) == 11
    assert sum_of_digits(45002) == 11
    assert sum_of_digits(8) == 8
    assert sum_of_digits(0) == 0


########################################
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
    pytest.main([
        "-v",
        "--no-header",
        "-s", # 'print' output
        "-W", "ignore::pytest.PytestAssertRewriteWarning",
        __file__
    ])    
