import re

name = "Maarison"
x = re.search("^M.*n$", name)

if x :
    print("Its Correct")
else:
    print("Its Incorrect")