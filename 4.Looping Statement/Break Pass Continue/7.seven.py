# 7. Print characters of a string, skipping vowels.

name = "Maarison"

for i in name:
    if i in "aeiouAEIOU":
        continue
    print(i)
