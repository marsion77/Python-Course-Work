# 10. Iterate over numbers from 1 to 10, skip 5 and stop at 8.

for i in range(1,11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
