# 1.Append Method
list = [1,2,3,4,5]
list.append(6)
print(list)
list.append("seven")
print(list)


# 2.Clear Method
names = ["Maarison","Maasi"]
print(names)
names.clear()
print(names)

# Remove Method
n = ["Maarison","Manoj"]
n.remove("Maarison")
print(n)

# Pop Method
numbers = [0,1,2,3]
numbers.pop(0)
print(numbers)

# 3.Copy Method
one = [1,2,3,4]
two = one.copy()
print(two)


# 4. Access List Items via Index
items = ["one","two","three","four","five","six","seven"]
print(items[0])
print(items[2])
print(items[1:2])
print(items[0:2])
print(items[-2:-1])

# 5.Change index Value
fruits = ["apple","banana","Grapes"]
fruits[0]="orange"
print(fruits)

# 6.Insert Method
fruits.insert(2,"Guava")
print(fruits)


# 7.Count Method
a = [1,2,5,3,4,5,6,7,5,7,8,9,0]
print(a.count(5))

# 8.Extend Method
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

n1.extend(n2)
print(n1)
print(n2)

#9. Index Method
c = [1,2,3,4,5]
d = c.index(2)
print(d)

# 10. Reverse Method
datas = [5,4,3,2,1]
datas.reverse()
print(datas)

#11. Sort Method
alpha = ["ball","apple","dog","cat","fish","elephant"]
alpha.sort()
print(alpha)