# gol ya puch

import random

x = input("Gol ya Puch? ")

if x == "gol" or x == "Gol":
    x = 1
elif x == "puch" or x == "Puch":
    x = 0
else:
    print("The response was unclear. Please try again.")

y = random.randint(0,1)
# print(y)

if y == x:
    print("Congratulations, you won.")
elif y != x:
    print("Sorry, you lost.")