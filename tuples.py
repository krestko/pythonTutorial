#tuples cannot be altered after creation
pi_tuple = (3, 1, 4, 1, 5, 9)
#convert a tuple into a list so that it can be altered
new_list = list(pi_tuple)
#convert a list back into a tuple
new_tuple = tuple(new_list)
#retrieve length of a tuple
print(len(pi_tuple))
#retrieve largest of a tuple
print(max(pi_tuple))
#retrieve smallest of a tuple
print(min(pi_tuple))
