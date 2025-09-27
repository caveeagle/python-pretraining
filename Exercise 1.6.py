
import random

#seed = None
seed = 12

random.seed(seed)

x = []

for _ in range(7):
    x.append(random.randint(15,25))

print(x)

#######################

average = sum(x)/len(x)

# Calculate median:

sorted_list = sorted(x) # create new list

print(sorted_list)

middle = len(x)//2 # floor division

if( len(x)%2 ):
    mediana = sorted_list[middle]
else:
    mediana = (sorted_list[middle-1]+sorted_list[middle])/2

print('mediana:',mediana)

#######################
