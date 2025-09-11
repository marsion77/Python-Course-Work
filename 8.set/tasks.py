# SET TASKS

myset = {"one","two","three","four","five"}
print(myset)
print(len(myset))
print(type(myset))

# using Constructor Method to create a set
newset = set(("one","two","three"))
print(newset)

newtuple = tuple(("1","2","3"))
print(newtuple)

newlist = list(("one","two","three","four","five"))
print(newlist)

# Loop through set
setdata = {1,2,3,4,5,True,False,"True","False",True,7,9,10}
for i in setdata:
    print(i,"Looping through set")

# Access values in set
fruitset = {"apple","banana","cherry"}
print("banana" in fruitset)

# Add value in set
fruitset.add("grapes")
print(fruitset)