inventory = {'gold' : 500,
             'pouch' : ['flint', 'twine', 'gemstone'], 
             'pouch' key
             'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
             }


# Adding a key 'burlap bag' and assigning a list to it


inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell', 'strange berry', 'lint']


# Sorting the list found under the key 'pouch'


inventory['pouch'].sort()
inventory['backpack'].sort()


# Here the dictionary access expression takes the place of a list name


inventory['backpack'].remove('dagger')

inventory['gold'] = inventory['gold'] + 50

print inventory['gold']