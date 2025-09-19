from functools import reduce
fact = reduce(lambda x,y: x*y,range(1,6))
print(fact)