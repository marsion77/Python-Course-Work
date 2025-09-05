# 1. Odd Or Even
a = int(input("Enter a Number"))
if a % 2 == 0:
    print("The Entered Numbet is Even")
else:
    print("The Entered Number is Odd")

# 2.Divisible By 5
a = int(input("Enter a Number"))
if a % 5 == 0:
    print("The Number is Divisible by 5")
else:
    print("The Number is Not Divisible by 5")

# 3.Greater Than Less Than
a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))
if a > b:
    print("First Number is Greater than the Second")
elif a == b:
    print("Both A and B are Equal")
else:
    print("Second Number is Greater than the First")

# 4.Substring
name = "Maarison"
if "son" in name:
    print(True)
else:
    print(False)

# 5.Range Task
a = int(input("Enter a Number"))
if a in range (1,11):
   print("The Number is in range between 1 to 10")
else:
   print("The Number is not in rage between 1 to 10")
b = 9
if b < 10 and b > 0:
   print("The Number is range between ")
else:
   print("Not in range")

# 6.Vovel
a = input("Enter a Character")
b = (a.upper())
if b == "A" or b == "E" or b == "I" or b == "O" or b == "U":
    print("The Character You have Entered is a Vovel")
else:
    print("The Character You have Entered is Not a Vovel")

# 7.Vote Eligiblity
age = int(input("Enter Your Age"))
if age >= 18:
    print("You are Eligible to Vote")
else:
    print("You are Not Eligible to Vote")

