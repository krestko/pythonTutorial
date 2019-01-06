#python objects
family = { 'Older Brother' : 'Matt',
           'Younger Brother' : 'Dan',
           'Mom' : 'Joan',
           'Dad' : 'Michael' }
print(family)
#find value of a particular key
print(family['Mom'])
#or
print(family.get('Mom'))
#remove a key/value pair from dictionary
del family['Dad']
print(family)
#change value of a key
family['Younger Brother'] = 'Michael'
print(family)
#find length of dictionary
print(len(family))
#retrieve a list of dictionary keys
print(family.keys())
#retrieve a list of dictionary values
print(family.values())