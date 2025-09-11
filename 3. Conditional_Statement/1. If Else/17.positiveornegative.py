a = int(input("Enter a Number"))

if a == 0:
    print("The Number is Neither Positive Nor Negative")
elif a < 0:
    print("The Number is Negative")
elif a > 0:
    print("The Number is Positive")
else:
    print("Enter a Valid Number")