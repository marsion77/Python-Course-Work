# 1. Print numbers from 1 to 10, but stop when the number is 5.
for i in range(1,11):
    if i == 5:
        break
    print(i)

# 2. Find the first negative number in a list.
list = [1,2,-3,4,5,-3,5,7,7,7]

for i in list:
    if i < 0:
        print(i)

# 3.Iterate over a list and stop if you encounter a zero.
list = [1,2,3,4,0,5,60,3,4,5,6,70,0]
for i in list:
    if i == 0:
        break
    print(i)

# 4. Print numbers from 1 to 10, skipping 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# 5.Print only even numbers from 1 to 10. 
for i in range(1,11):
    if i % 2 == 0:
        print(i)


# 6. Iterate over a list and skip negative numbers.
list = [1,-1,2,-2,3,-3,4,-4,5,-5]
for i in list:
    if i < 0:
        continue
    print(i)

# 7. Print characters of a string, skipping vowels.
name = "Maarison"
for i in name:
    if i in "aeiouAEIOU":
        continue
    print(i)

# 8.Iterate over numbers from 1 to 20, but skip multiples of 3.
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

# 9. Iterate over a list and use pass for future implementation.
list = ["One","Two","Three"]
for i in list:
    pass

# 10. Iterate over numbers from 1 to 10, skip 5 and stop at 8.
for i in range(1,11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)

# 11.Print only odd numbers from 1 to 10, but use pass for even numbers.
for i in  range(1,11):
    if i % 2 == 1:
        print(i)
    if i % 2 == 0:
        pass

# 12.Iterate over a list, skip negatives, print positives, stop at zero.
list = [1,2,3,4,5,-1,-2,-3,-4,-5,0,1,2,3,4,5]
for i in list:
    if i < 0:
        continue
    if i == 0:
        break
    print(i)

# 13.Skip the first half of a list, process the second half, use pass for future.
numbers = [9,4,6,2,4,6,7,9] 

first_half = len(numbers) // 2  

for i in range(len(numbers)):
    if i < first_half: 
        continue    
        print(numbers[i])


# 14.Get a input from user like number until user enter zero after that have to print the product of numbers.

num = int(input("Enter a number (0 to stop): "))
product = 1
while num != 0:
    product = product * num
    num = int(input("Enter a number (0 to stop): "))
print("Product:", product)



# 15.Get a input from user like number until user enter negative number after that have to print the sum of numbers

num = int(input("Enter a number (0 to stop): "))
sum = 0
while num != 0:
    sum = sum +  num
    num = int(input("Enter a number (0 to stop): "))

print("Sum:", sum)
