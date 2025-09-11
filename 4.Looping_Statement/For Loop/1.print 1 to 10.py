# 1.Print numbers 1 to 10
for i in range(1,11):
 print(i)

# 2.Print the square of each number from 1 to 10
for i in range(1,11):
    i = i * i
    print(i)

# 3.Print each character in a string
name = "Maarison Marikozhundu"
for i in name:
    print(i)

# 4.Sum of numbers from 1 to 10
add = 0
for i in range(1,11):
    print(i)

# 5.Print each element in a list
vehicle = ["suzuki","acccess","Activa","pulsar"]
for i in vehicle:
    print(i)

# 6.Print numbers from 10 to 1 (reverse order)
for i in range(10,0,-1):
    print(i)

# 7.Print only even numbers from 10 to 20
for i in range(10,21):
    if i % 2 == 0:
        print(i)

# 8.Print the multiples of 5 between 20 to 50 .
for i in range(20,51):
    if i % 5 == 0:
        print(i)

# 9.Print the factorial of a number
factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)



# 10.Print numbers from a list that are greater than 10
numbers = [5,3,78,90,2,45,2,10,]
for i in numbers:
        if i > 10:
            print(i)


# 11.Print all prime numbers between 10 and 20
for num in range(10,21):
    if num > 1:
            if (num % 1) == 0 and (num % num)==0:
                 print(num)

# 12.Find the largest number in a list 
numbers = [5,3,78,90,2,45,2,10,]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)


# 13.Count the number of vowels in a string
string = "Maarison Marikozhundu"
count = 0
for i in string:
    if i in 'aeiouAEIOU':
        count = count + 1
        print(count)

# 14.Print product of 1 to 5
product = 1
for i in range(1,6):
    product = product * i
print(product)

# 15.Get a input from user like number until user enter zero after that have to print the product of numbers.
product = 1
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0: 
        break
    product *= num

print(product)

# 16.Get a input from user like number until user enter negative number after that have to print the sum of numbers.
sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num < 0:
        break
    sum += num
print(sum)


















