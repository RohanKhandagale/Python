# write a code to pick a random name form list
import random
friends =["Rohan","Sohan","Rajesh","Suraj","Pratik"]
# .choice is use to choose a random item in list
print(random.choice(friends))

# 2 way
random_index = random.randint(0,4)
print(friends[random_index])