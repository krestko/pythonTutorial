import random
#for loop for range. Does not include second number.
for x in range(0, 10) :
  print(x, '', end='')

print('\n')

#for loop for predefined lists
grocery_list = ["juice", "tomatoes", "potatoes", "bananas"]
for y in grocery_list :
  print(y)

#define list in for loop
for x in [2, 4, 6, 8, 10] :
  print(x)

#nested loops
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3) :
  for y in range(0, 3) :
    print(num_list[x][y])

#while loops, used when you don't know how many values will be looped through
i = 0

while(i <= 20) :
  if(i % 2 == 0) :
    print(i)
  elif(i == 9) :
    break
  else :
    i += 1
    continue
  i += 1

print('\n')

random_num = random.randrange(0, 100)
print(random_num)

while(random_num != 15) :
  print(random_num)
  random_num = random.randrange(0, 100)



