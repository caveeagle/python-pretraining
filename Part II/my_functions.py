
#################################
 
def multiplication(x, y):
    return x*y

assert multiplication(3,5)==15

#################################

# Take a string as input and return `True` if the string 
# is a palindrome (reads the same backward and forward) 
# and `False` otherwise.

def is_palindrome(text:str):
    
    chars = list(text)
    
    chars.reverse()
    
    reversed_text = ''.join(chars)
    
    return ( True if text == reversed_text else False )
    
    
assert is_palindrome('ABC')==False
assert is_palindrome('ASDF5FDSA')==True

#################################

print('All tasks are completed!')
    
 