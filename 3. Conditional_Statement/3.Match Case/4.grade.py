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


