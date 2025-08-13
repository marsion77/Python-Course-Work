# Global Variables
x = 5
def f1():
    print(x)
f1()   


# variable Inside the Function
y = 87
def f2():
    y = 77
    print(y)
f2()
print(y)


# Variable with the Keyword Variable

z = 10

def f3():
    global z
    z = 5
    print(z)

f3()
print(z)



