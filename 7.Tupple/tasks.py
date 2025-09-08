# Access Tuple 
mytuple = ("Apple","Banana","Cherry","Grapes","Pineapple")
print(mytuple)
print(mytuple[0])
print(mytuple[1:2],": indexing")
print(len(mytuple))


# Looping Tuple
for i in mytuple:
    print(i)


# Updating Tuple ADD
names = (1,2,3,4,4,-1)
ordered = list(names)
ordered[4] = 5
names = ordered
print(ordered," modified a tuple")


# Remove
removed_list = list(names)
removed_list.remove(-1)
names = removed_list
print(removed_list,"Removed a item from the tuple")


# Unpack Tuple
pack_list = (1,2,3)
(one,two,three) = pack_list
print(1)
print(2)
print(3)


# Using Asterisk
another_list = (1,2,3,4,5,6,7,8,9,10)
(first,second,*third) = another_list
print(first)
print(second)
print(third)

# Count
listdata = (1,2,2,3,2,3,2,4,5,6,78,0)
print(listdata.count(2),"Count Method")