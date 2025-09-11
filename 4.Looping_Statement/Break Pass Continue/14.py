# 14.Get a input from user like number until user enter zero after that have to print the product of numbers.

num = int(input("Enter a number (0 to stop): "))
product = 1

while num != 0:
    product *= num
    num = int(input("Enter a number (0 to stop): "))

print("Product:", product)
