month = 1

match month:
    case 1|3|5|7|8|10|12:
        print("This Month has 31 Days")
    case 4|6|9|11:
        print("This Month has 30 Days")
    case 2:
        print("The Month has 28 or 29 Days")
    case _:
        print("Enter a Number between 1 to 12")


# 3.print a entered input is vowels or consonants.
letter = "a"

match letter:
    case "a"|"e"|"i"|"o"|"u":
        print("The Letter is Vovel")
    case _:
        print("The Letter is not a Vovel")


# 4.grade by percentage.
mark = int(input("Enter a Number"))

match mark:
    case _ if mark > 0 and mark <= 30:
        print("You are Failes")
    case _ if mark > 30 and  mark<= 50:
        print("You are C Grade")
    case _ if mark > 50 and mark<= 70:
        print("You are B Grade")
    case _ if mark > 70 and mark <=90:
        print("You are A grade")
    case _ if mark > 90 and mark<= 100:
        print("You are A+ Grade")
    case _:
        print("Enter a Valid Number")

# month = int(input("Enter a Month Number Here"))

match month:
    case 1|2|3|4:
        print("The Month is Winter")
    case 5|6|7|8:
        print("The Month is Summer")
    case 9|10|11|12:
        print("The Month is Rainy")
    case _:
        print("Enter a Valis Month Number")


# 6.positive or negative
number = 2

match number:
    case _ if number > 0:
        print("The Number is Positive")
    case _ if number == 0:
        print("The Number is Neither Ngative Nor Postive")
    case _:
        print("The Number is Negative")


# 7.Range
number = int(input("Enter a Number"))

match number:
    case _ if number in range(1,51):
        print("The Number is in Range 1 to 50")
    case _:
        print("The Number is Not in Range between 1 to 50")




