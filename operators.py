# Assignment Operator
a = 10
b = 20


# Arithmetic Operator
print(a+b,"Arithmetic Operator")
print(a-b)
print(b%a)


# Python Comparison Operator
print(a == b)
print (a<b,"Comparison Operator")
print(b>b)


# Logical Operator
print(a<0 and b<0,"Logical Operator")
print(a<0 or b>0)


# Membership Operator
c = ["Car","Bike"]
d = ["Bicycle","Scooter"]
e = c
print("Car" in c,"Menbership Operator")
print("Bike" not in c)


# Identity Operator
print(c is e,"Identity Operator")
print (c is d)

if a<b:
    print("a is less than b")