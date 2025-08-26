Number = int(input("Enter a Number"))

if Number % 5 == 0 and Number % 11 == 0:
    print("The Number is Divisible By Both 5 and 11")
elif Number % 5 == 0:
    print("The Number is Divisible By 5")
elif Number % 11 == 0:
    print("The Number is Divisible By 11")
else:
    print("The Number is Noit Divisible by Both 5 and 11")
