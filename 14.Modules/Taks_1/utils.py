def factorial(n):
    if n == 0:
          return 1
    else:
           return n * factorial(n - 1)
   


def prime(n):
        if n <= 1:
              return False
        if n <= 3:
              return True
        if n % 2 == 0 or n % 3 == 0: 
              return False
        else:
              return False