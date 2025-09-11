Year = int(input("Enter a Year"))

if Year % 400 == 0 or (Year % 100 != 0 and Year % 4 == 0):
    print("The Year is Leap")
else:
    print("The Year is Not Leap")