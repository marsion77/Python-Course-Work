Number_One = int(input("Enter the First Number"))
Number_Two = int(input("Enter the Second Number"))
Number_Three = int(input("Enter the Third Number"))

if Number_One > Number_Two and Number_One > Number_Three:
    print("Number 3 is Greater that other 2 Numbers")
elif Number_Two > Number_One and Number_Two > Number_Three:
    print("Number 2 is Greater than other 2 Numbers ")
elif Number_Three > Number_One and Number_Three > Number_Two:
    print("Number 1 is Greater than Other 2")
elif Number_One == Number_Two and Number_Two == Number_Three:
    print("All are Equal Numbers")