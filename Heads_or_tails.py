import random

#coin_toss is equal to a randomly generated integer between 0 and 1
coin_toss = random.randint(0,1)

#if the random integer is equal to 0 it's heads, if not, then it's tails
if coin_toss == 0:
    print("Heads")
else:
    print("Tails")