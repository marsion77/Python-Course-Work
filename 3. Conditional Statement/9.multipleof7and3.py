Number = int(input("Enter a Number"))

if Number % 3 == 0 and Number % 7 == 0:
    print("The Number is Divisible By Both 3 and 7")
elif Number % 3 == 0:
    print("The Number is Divisible By 3")
elif Number % 7 == 0:
    print("The Number is Divisible By 7")
else:
    print("The Number is Noit Divisible by Both 3 and 7")
