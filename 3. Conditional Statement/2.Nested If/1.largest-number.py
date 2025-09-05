# 1. Find Greatest Number
first = 20
second = 8
third = 9

if first > second:
    if first > third:
        print("First Number is Greatest")
    else:
        print("Third Number is Greatest")
else:
    if second > third:
        print("Second Number is Greatest")
    else:
        print("Third Number is Greatest")



# 2. Divisble By 5 and 7
number = 55

if number % 5 == 0:
    if number % 11 == 0:
        print("The Number is Divisible By Both 5 and 7") 
else:
    print("The Number is Not divisible by Both 5 and 7")



# 3.Check if a number lies in the range 10-50.
number = int(input("Enter a Number"))

if (number > 0 ):
    if (number > 10 and number <= 50):
        print("The Number is range between 10 and 50")
    else:
        print("The Number is not in range between 10 and 50")

else:
    print("Enter Positive Numbers")


# 4.Check if a year is a leap year or not
year = int(input("Enter a Year: "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("The Year is a Leap Year")
    else:
        print("The Year is Not a Leap Year")
else:
    print("The Year is Not a Leap Year")


# 5.Check if a number is positive and even.
number = int(input("Enter a Number"))

if number > 0:
    if number % 2 == 0:
        print("The Number is Both Positive and Even")
    else:
        print("The Number is Odd")
else:
    print("The Number is Negative Number") 


# Match case
# 1.Check a day as weekday or weekend.
day = 1
match day:
    case 1 |2|3|4|5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Enter a Number Between 1 to 7")

# 2.print a no of days in a month.
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

#5 month = int(input("Enter a Month Number Here"))

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











