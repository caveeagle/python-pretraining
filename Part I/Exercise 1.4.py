
#1. Create a list of 10 famous artists and print the list.

artists_raw_list = '''
Leonardo da Vinci
Monet
Vincent van Gogh
Picasso
Rembrandt
Dali
Michelangelo
Renoir
Chagall
Matisse
'''

artists = artists_raw_list.splitlines()

artists = list(filter(None, artists)) # Remove empty strings

# *!*  filter(None, iterable) - remain only 'True' elements 

print( f"I've found {len(artists)} artists:\n{artists}" )

#2. Add a famous artist to the list of artists and print the updated list.

artists.append('Banksy')
print(artists)

#3. Order the list alphabetically and print the three first artists.

artists.sort(key=str.lower)

# *!* sort() modifies the original list!
# *!* sorted() returns a new list!

print(artists[:])
print(artists[0:3])

#4. Create a tuple containing three famous artworks and print the tuple.

artworks_raw_list = '''Mona Lisa
Starry Night
The Persistence of Memory
'''

artworks_list = artworks_raw_list.splitlines()

artworks_tuple = tuple(artworks_list)

print("\n" * 5) # Print vert.space

print(artworks_tuple)

# Add element to immutable tuple

artworks_tuple = artworks_tuple + ('Guernica',)

print(artworks_tuple)

#5. Create a set of art styles
#7. Create a second set of art styles and print the common elements.

artstyles_old = {'Baroque','Realism','Minimalism','Impressionism','Expressionism','Cubism','Futurism'}

artsyles_new = {'Surrealism','Abstract Art','Pop Art','Minimalism','Futurism','Realism'}

print( f"Common elements in styles: {artstyles_old.intersection(artsyles_new)}" )

#8. Create a dictionary with famous artists as keys and their most known artwork as values.
#9. Add a new artist and his/her most famous artwork to the existing dictionary and print it.
#10. Access the most famous artwork of a specific artist in the dictionary and print it.
#11. Remove an artist and his/her artwork from the dictionary and print the updated dictionary.

# Create: 
artworks = {}

artworks['Leonardo da Vinci']='Mona Lisa'
artworks['Vincent van Gogh']='Starry Night'

# Add with checking:
artist = 'Rembrandt'
artwork='The Night Watch'

if(artist not in artworks):
    artworks[artist] = artwork

artist = 'Pablo Picasso'
artwork='Guernica'

# Add with default value:
artworks.setdefault(artist,artwork) 
artworks.setdefault(artist,'Unknown art') # Nothing to do if key artist exists

artworks['Claude Monet'] = 'forgery'
# Ups... Sorry, I’ll delete it now:
del artworks['Claude Monet']

print('\n'*3,artworks)

# find by value:
value = 'Starry Night2'
found_keys = [k for (k, v) in artworks.items() if v == value]

if(len(found_keys)>1):
    pass
elif(len(found_keys)==0):
    raise KeyError("Key not found")
else:
    print( f'Artist {found_keys[0]} draw {value}' )

###################################################


