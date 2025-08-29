number = 2

match number:
    case _ if number > 0:
        print("The Number is Positive")
    case _ if number == 0:
        print("The Number is Neither Ngative Nor Postive")
    case _:
        print("The Number is Negative")

