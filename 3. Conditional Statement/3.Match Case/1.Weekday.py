day = 1
match day:
    case 1 |2|3|4|5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Enter a Number Between 1 to 7")
