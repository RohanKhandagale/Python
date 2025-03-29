import random
a = "Heads"
b = "Tails"
random_coin = random.randint(0,1)
if random_coin == 0:
    print(a)
else:
    print(b)