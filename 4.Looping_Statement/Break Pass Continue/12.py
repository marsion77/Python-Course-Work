# 12.Iterate over a list, skip negatives, print positives, stop at zero.

list = [1,2,3,4,5,-1,-2,-3,-4,-5,0,1,2,3,4,5]

for i in list:
    if i < 0:
        continue
    if i == 0:
        break
    print(i)
