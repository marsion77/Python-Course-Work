my_list = ["apple","banana","app","ban"]
shorter4 = list(filter(lambda x: len(x)<=4,my_list))
print(shorter4)