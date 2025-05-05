programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


# for adding new item in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Loop"])

# wipe the dictionary
# programming_dictionary = {}
# print(programming_dictionary)
# print(programming_dictionary["Loop"])

# loop through dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])