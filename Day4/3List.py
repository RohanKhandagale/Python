fruits =["mango","apple","banana","graphs"]

# we can get list data by their index numbers it start from 0 to further on
print(fruits[3])

# we can also modified the list
fruits[1] = "Chiku"
print(fruits)

# .append is used to add one item to end of the list . extend is used to multiple items to end of the list
fruits.append("Watermelon")
print(fruits)
fruits.extend(["Dragonfruit","custard apple","Kiwi"])
print(fruits)
fruits.remove("custard apple")
print(fruits)