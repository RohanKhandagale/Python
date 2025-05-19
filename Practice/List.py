# finding different datatypes in list int str
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango",1,5,55,66,78,"hero",True,True,False]
search = input("Find in list:-")

# insert() is used to insert a data in provided index
thislist.insert(2,"peru")
thislist.append("Moh")

# for searching int data type int and bool
if search.isdigit():
    search = int(search)
elif search.lower() =="true":
    search = True
elif search.lower() == "false":
    search = False

if search in thislist:
    print("yes")
else:
    print("NO")

print(thislist)