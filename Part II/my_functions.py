
#################################
 
def multiplication(x, y):
    return x*y

assert multiplication(3,5)==15

#################################

def is_palindrome(text:str):
    '''
     1. Take a string as input and return `True` if the string 
     is a palindrome (reads the same backward and forward) 
     and `False` otherwise.
    '''    
    chars = list(text)
    
    chars.reverse()
    
    reversed_text = ''.join(chars)
    
    return ( True if text == reversed_text else False )
    
    
assert is_palindrome('ABC')==False
assert is_palindrome('ASDF5FDSA')==True

#################################

def reverse_string(text:str):
    '''
     9. Take a string and return the reversed word ("bla" > "alb")
    '''

    chars = list(text)
    
    chars.reverse()
    
    reversed_text = ''.join(chars)
    
    return reversed_text

assert reverse_string('bla') == 'alb'    

#################################

def is_divisible(x, y):
    '''
     Take two numbers and check if the first one is divisible by the second one
    '''
    if not isinstance(x, (int, float)):
        raise TypeError('Argument `x` must be int or float')
        
    if not isinstance(y, (int, float)):
        raise TypeError('Argument `y` must be int or float')
    
    if(y==0):
        raise ZeroDivisionError("Division by zero is not allowed")
    
    remainder = x % y
   
    return remainder==0

assert is_divisible(30,10) == True  
assert is_divisible(31,20) == False  

#################################

def get_initials(text:str):
    '''
     3.Take a full name and return the initials ("Becode Ghent" > "BG")
    '''
    
    result = ''
    
    words = text.split()
    
    for word in words:
        first_char = word[0]
        result += first_char
    
    return result

assert get_initials("Becode Ghent")=="BG"

#################################

def longest_word(words:list):
    '''
     Take a list of words as input and return the longest word in the list
    '''
    # WE USE max(iterable, key=fn)
    
    result = max(words, key=lambda x: len(x))
    
    return result

#################################

def sum_of_digits(number:int):
    '''
     Take an integer and return the sum of its digits
    '''
    digits = []
    
    while number>0:
        
        digit = number % 10
        
        digits.append(digit)
        
        #print(digit)
        
        number = number // 10 # integer division
    
    return sum(digits)    

assert sum_of_digits(123)==6
    
#################################

def password_validation(password:str):
    '''
     Take a password and validate it by returning `True` or `False` 
     (conditions: more than 8 characters, at least one not alpha-numerical character)
    '''

    has_special = False
    for char in password:
        if not char.isalnum():
            has_special = True
            break

    return ( not password.isalnum() )and( len(password)>8 )

#################################
#################################

print('All tasks are completed!')
    
 