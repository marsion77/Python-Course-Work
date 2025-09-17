# Python Functions

# 1. Calculate Square
def square(n):
   return n*n
print(square(2))

# 2.Calculate Area of a Rectangle
def area_of_rextangle(lenghth,width):
   return lenghth * width
print(area_of_rextangle(lenghth=10,width=20))

# 3.Check Even or Odd
def odd_or_even(n):
   if n % 2 == 0:
      return "Even"
   else:
      return "odd"
print(odd_or_even(7))

# 4.Calculate Factorial
def factorial(n):
   pass

# 5.Prime Number
# def prime_number(n):
#    if n > 1 and n % n == 0 and n % 2 !=1:
#       return "Prime Number"
#    else:
#       return "Not a Prime Number"
# print(prime_number(6))
   

# 6.Reverse a String
def reverse(str):
   return str[::-1]
print(reverse("Maarison"))

# 7.Count Characters
def caharcerscount(word):
   return word.count("a")   
print(caharcerscount("Maarison"))

# 8.Sum of Squares
def sum_of_squares(i,j):
   return i * i + j * j
print(sum_of_squares(8,8))


# 9.Palindrom
def palindrom(name):
   if name == name[::-1]:
      return True
   else:
      return False
print(palindrom("Mom"))

# 10.Febonacci


# 11.Armstrong Number