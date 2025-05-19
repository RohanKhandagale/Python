thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango",1,5,55,66,78,"hero",True,True,False]
myList = ["Rohan","Khandagale",88,99,100]
my_tuple = ("Good","Bad","Nothing")

# extend is used to merge the data in one order tuple,list etc
# thislist.extend(my_tuple)
# myList.extend(my_tuple)

# .remove is used when removes specific item
thislist.remove("apple")

# .pop is used when removes specific index
thislist.pop(2)
for item in thislist:
    print(thislist)


print(myList)
print(thislist)