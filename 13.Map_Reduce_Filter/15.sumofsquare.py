from functools import reduce
my_list = [1,2,3,4,5]
sum_of_square = list(map(lambda x: x*x,my_list))
square = reduce(lambda x,y: x+y,sum_of_square)

print(square)

