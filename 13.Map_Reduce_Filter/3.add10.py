
# Map
my_lsit = [1,2,3,4,5,6,7,8,9,10]
square = lambda x : x * 2
doubled = list(map( square , my_lsit))
print(doubled)

# Filter
my_data = [1,2,3,4,5,6,7,8,9,10]
odd = lambda x : x % 2 == 0
odded = list(filter(odd,my_data))
print(odded)


# reduce
import functools
my_values = [1,2,3,4,5,6,7,8,9,10]
total = functools.reduce(lambda x,y: x + y , my_values)
print(total)