month = int(input("Enter a Month Number Here"))

match month:
    case 1|2|3|4:
        print("The Month is Winter")
    case 5|6|7|8:
        print("The Month is Summer")
    case 9|10|11|12:
        print("The Month is Rainy")
    case _:
        print("Enter a Valis Month Number")
