grocery_list = ["juice", "tomatoes", "potatoes", "bananas"]
print('first item is', grocery_list[0])
#change value of a list
grocery_list[0] = "green juice"
print('first item is', grocery_list[0])
#print up to but not uncluding values from list
print(grocery_list[0:3])
#lists inside lists
other_events = ["wash car", "pick up kids", "cash check"]
to_do_list = [other_events, grocery_list]
print(to_do_list)
#print second item from first list
print(to_do_list[0][1])
#add item to the end of a list
grocery_list.append('onions')
print(grocery_list)
#add item to particular place within a list
grocery_list.insert(1, "pickle")
print(grocery_list)
#remove particular item using name of item
grocery_list.remove("pickle")
print(grocery_list)
#remove particular item using index of item
del grocery_list[0]
print(grocery_list)
#sort items within a list
grocery_list.sort()
print(grocery_list)
#reverse the list
grocery_list.reverse()
print(grocery_list)
#merge lists
to_do_list2 = grocery_list + other_events
print(to_do_list2)
#find length of list
print(len(to_do_list2))
#will find the largest value. If it is string it will be based on alphabetical sort
print(max(to_do_list2))
#will find the smallest value
print(min(to_do_list2))