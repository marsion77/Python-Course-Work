# 2. Find the first negative number in a list.
list = [1,2,-3,4,5,-3,5,7,7,7]

for i in list:
    if i < 0:
        break
print(i)


    