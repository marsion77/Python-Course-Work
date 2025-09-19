from functools import reduce
my_list = [1,2,3,7,5,4,2]
maxnum = reduce(lambda x,y: x if  x>y else y,my_list)
print(maxnum)