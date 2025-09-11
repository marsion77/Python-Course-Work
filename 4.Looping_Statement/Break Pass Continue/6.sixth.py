# 6. Iterate over a list and skip negative numbers.

list = [1,-1,2,-2,3,-3,4,-4,5,-5]

for i in list:
    if i < 0:
        continue
    print(i)
