from functools import reduce
my_list = ["one","two","three"]
concate = reduce(lambda x,y: x+y,my_list)
print(concate)