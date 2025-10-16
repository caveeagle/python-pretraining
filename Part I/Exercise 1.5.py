
# Determine if a number is even or odd

x = 50

assert type(x) is int, "var. x must be int"

if( x%2 == 0 ):
    print('Even')
else:
    print('Odd')    


# Print the largest number among 3 numbers

a = 3
b = 3
c = 3

if( a>=b and a>=c ): 
    print(a)
elif( b>=a and b>=c ): 
    print(b)
elif c>=a and c>=b : 
    print(c)
else: 
    raise RuntimeError("Algorithmic error")
    

# Check wheter a letter is a vowel or a consonant

char = 'i'

vowel = ('a','e','i','o','u''A','E','I','O','U')

assert len(char)==1 and type(char) is str

if( char in vowel ):
    print('vowel')
else:
    print('consonant')    

# Create a Python program that checks if a given character 
# is an uppercase letter, a lowercase letter, a digit, or a special character

ch = 'с'

if( ch.islower() ):
    print('lowercase')

if( ch.isupper() ):
    print('uppercase')
    
if( ch.isdigit() ):
    print('digit')

if not ch.isalnum():
    print('special character')

#######################
