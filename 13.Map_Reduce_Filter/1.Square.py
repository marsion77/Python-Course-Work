# 1.Square a Number
my_list = [1,2,3,4,5]
squared = list(map(lambda x: x*x,my_list))
print(squared)

# 2.Capitalise String
a = "maarison"
capitalise = list(map(lambda x: x.upper(),a))
print(capitalise)

# 3.Add 10 to elemt in a list
my_list = [1,2,3,4,5]
added_10 = list(map(lambda x: x+ 10,my_list))
print(added_10)

# 4.Double the Number
my_list = [1,2,3,4,5]
added_10 = list(map(lambda x: x+x,my_list))
print(added_10)

# 5.Capilaise First Letter of a String
my_list = ["apple","babana","grapes"]
cap = list(map(lambda x: x.capitalize(),my_list))
print(cap)


# 6.Filter Even
my_list = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x%2==0,my_list))
print(evens)

# 7.Filter out words shorter than 4 characters
my_list = ["apple","banana","app","ban"]
shorter4 = list(filter(lambda x: len(x)<=4,my_list))
print(shorter4)


# 8.Filter out numbers greater than 10
my_list = [1,2,3,4,5,12,13,14,14]
great_8 = list(filter(lambda x: x >8,my_list ))
print(great_8)

# 9.Filter out strings containing the letter 'a'
my_list = ["apple","banana","dog"]
shorter4 = list(filter(lambda x: "a" in x,my_list))
print(shorter4)

# 10.Not Divisibel by 3
my_list =[1,2,3,4,5,6,7,8,9,10]
div_3 = list(filter(lambda x: x % 3 != 0 , my_list))
print(div_3)

# 11.Filter Negative
my_list = [-1,1,-2,2,-3,3,-4,4,-5,5]
negative = list(filter(lambda x: x < 0,my_list))
print(negative)

# 12.Product of a Number
from functools import reduce
my_list = [1,2,3,4,5,6,7,8,9,10]
product = reduce(lambda a,y: a * y,my_list)
print(product)

# 13.Concate
from functools import reduce
my_list = ["one","two","three"]
concate = reduce(lambda x,y: x+y,my_list)
print(concate)

# 14.Max Number
from functools import reduce
my_list = [1,2,3,7,5,4,2]
maxnum = reduce(lambda x,y: x if  x>y else y,my_list)
print(maxnum)


# 15.Sum of Square
from functools import reduce
my_list = [1,2,3,4,5]
sum_of_square = list(map(lambda x: x*x,my_list))
square = reduce(lambda x,y: x+y,sum_of_square)
print(square)

# 16.Factorial
from functools import reduce
fact = reduce(lambda x,y: x*y,range(1,6))
print(fact)


