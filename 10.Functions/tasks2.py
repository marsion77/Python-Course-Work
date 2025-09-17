# Function 1: Calculate Square
def calculate_square(n):
    return n * n

# Function 2: Calculate Area of Rectangle
def area_rectangle(length, breadth):
    return length * breadth

# Function 3: Check Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function 4: Calculate Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Function 5: Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Function 6: Reverse a String
def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str

# Function 7: Count Characters
def count_characters(s):
    count = 0
    for _ in s:
        count = count + 1
    return count

# Function 8: Sum of Squares
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i * i)
    return total

# Function 9: Check Palindrome
def is_palindrome(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    if s == reversed_str:
        return True
    else:
        return False

# Function 10: Calculate Fibonacci
def fibonacci(n):
    seq = []
    a = 0
    b = 1
    if n >= 1:
        seq.append(a)
    if n >= 2:
        seq.append(b)
    for _ in range(2, n):
        c = a + b
        seq.append(c)
        a = b
        b = c
    return seq

# Function 11: Check Armstrong Number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = 0
    for digit in num_str:
        total = total + int(digit) ** power
    if total == n:
        return True
    else:
        return False

# Function 12: Check Leap Year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Function 13: Find index of duplicate elements in a list
def find_duplicates(lst):
    duplicates = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                if lst[i] not in duplicates:
                    duplicates[lst[i]] = [i]
                duplicates[lst[i]].append(j)
    return duplicates

# Function 14: Convert 3 lists into a Matrix
def lists_to_matrix(l1, l2, l3):
    matrix = []
    matrix.append(l1)
    matrix.append(l2)
    matrix.append(l3)
    return matrix

# Function 15: Paragraph to list and word count
def paragraph_to_list(paragraph):
    words = paragraph.split(" ")
    count = 0
    for _ in words:
        count = count + 1
    return words, count


# -------------------------------
# Sample Usage
if __name__ == "__main__":
    print("Square of 5:", calculate_square(5))
    print("Area of 4x6:", area_rectangle(4, 6))
    print("Check 7:", check_even_odd(7))
    print("Factorial of 5:", factorial(5))
    print("Is 29 Prime?:", is_prime(29))
    print("Reverse 'hello':", reverse_string("hello"))
    print("Count characters in 'Python':", count_characters("Python"))
    print("Sum of squares till 5:", sum_of_squares(5))
    print("Is 'madam' Palindrome?:", is_palindrome("madam"))
    print("First 7 Fibonacci:", fibonacci(7))
    print("Is 153 Armstrong?:", is_armstrong(153))
    print("Year 2024 Leap?:", is_leap_year(2024))
    print("Duplicates in [1,2,3,2,4,3]:", find_duplicates([1,2,3,2,4,3]))
    print("Matrix from 3 lists:", lists_to_matrix([1,2],[3,4],[5,6]))
    para = "Python is powerful and easy to learn"
    print("Words and count:", paragraph_to_list(para))
