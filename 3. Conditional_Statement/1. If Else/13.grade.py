Mark = int(input("Enter Your Mark Here"))


if Mark < 0 or Mark > 100:
    print("Enter Marks Between 1 to 100")
elif Mark <= 30:
    print("You Are Failed")
elif Mark in range(31,51):
    print("You are Grade C")
elif Mark in range(51,71):
    print("You are Grade B")
elif Mark in range(71,91):
    print("You are Grade A")
elif Mark in range(91,101):
    print("You are Grade A+")
