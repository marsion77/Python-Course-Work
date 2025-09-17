# Lambda Function Tasks

# 1.Sum 2 Numbers
a = lambda a,b: a+b
print(a(10,20),"Sum of two numbers")

# 2. Find max
b = lambda x, y: x if x > y else y
print(b(10,20),"Max Number")

# 3.Square a Number
c = lambda n : n * n
print(c(6),"Square of a number")

# 4.Reverse a string
d = lambda n: n[::-1]
print(d("Maarison"))

# 5.Check even
e = lambda n: "true" if n%2==0 else "false"
print(e(9),"Check Even or Odd")