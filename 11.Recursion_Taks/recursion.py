# Recursive Function Taks
# 1. Print 10 to 1
def f1(n):
    if n == 1:
        return 1
    else:
        print(n)
        return f1(n - 1)    
print(f1(10))




# 2.Print 1 to 10
def f2(n):
    if n == 10:
        print(n)
    else:
        print(n)
        f2(n + 1)
print(f2(1))




# 3.Fibonacci
def fibonacci(n):
    if n == 0:       
        return 0
    elif n == 1:      
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))



# 4.Sum of a list
mylist = [1,2,3,4,5]
def sumoflist(num):
    if not num:
        return 0
    else:
        return num[0]+sumoflist(num[1:])
print(sumoflist(mylist))



# 5.Factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5),"Factorial")

