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
