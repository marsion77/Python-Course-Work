number = int(input("Enter a Number"))

match number:
    case _ if number in range(1,51):
        print("The Number is in Range 1 to 50")
    case _:
        print("The Number is Not in Range between 1 to 50")