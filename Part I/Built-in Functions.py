
#    1. Find the length of the string `"Becode is fun!"` and print the result.

text = "Becode is fun!"

print(len(text))

#    2. Convert the string in a list of characters. Print its length.

print(len(list(text)))

#    3. Convert the list of characters in a `set`. Print its length. Can you explain the difference?

print(len(set(text)))

#    4. Create a list of numbers and print its lowest and highest values.

import random

random.seed(None)

x = []

for _ in range(10):
    x.append(random.randint(0,1024))

print( f"Max: {max(x)}, min:{min(x)}")

#    5. Print the sum of the elements of the list that you have created.

print(sum(x))

#    6. Sort the list in descending order and print it.

x.sort(reverse=True)

print(x)

#    7. Print the absolute value of `-42`.

print(abs(-42))

#    8. Create a string that contains a basic sum (like `"4 + 3"`). Find a way to print the result of that sum.

text = '14 + 15 + 1'

text_clean = text.strip()

str_list = text_clean.split('+')

int_list = [int(x) for x in str_list]

result = sum(int_list)

print(text+" = "+str(result))

#  The shortest way:

text = '2 + 3 + 9'

int_list = [int(x) for x in text.strip().split('+')]

print(text," = ",sum(int_list))


#    9. Round the decimal number `3.14159` to 2 decimal places, and print the result.

import math

print(f'Pi: {math.pi:.2f}')


#    10. Create a string with a number. Convert it to an integer and multiply it by `2`. Print the result.

text = '21'

print(  int(text)*2 )
