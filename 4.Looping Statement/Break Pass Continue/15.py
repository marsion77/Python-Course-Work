# 15.Get a input from user like number until user enter negative number after that have to print the sum of numbers

num = int(input("Enter a number (0 to stop): "))
sum = 0

while num != 0:
    sum += num
    num = int(input("Enter a number (0 to stop): "))

print("Product:", sum)
