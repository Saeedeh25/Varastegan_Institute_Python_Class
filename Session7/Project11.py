# mench
import random

p1 = input("first person, enter your color: ")
p2 = input("second person, enter your color: ")

takhte = [[1, " "], [2, " "], [3, " "], [4, " "], [5, " "], [6, " "], [7, " "], [8, " "], [9, " "], [10, " "], [11, " "], [12, " "], [13, " "], [14, " "], [15, " "], [16, " "], [17, " "], [18, " "], [19, " "], [20, " "]]

def dice():
    x = random.randint(1,6)
    return x

p = input("whos turn?")
if p == p1:
    while True:
        input(f"{p1}, roll the dice:")
        y = dice()
        print(f"{p1}, dice rolled. you got {y}")
        if y != 6:
            print("sorry, next ones turn.")
        elif y == 6:
            print("you can enter the bord.")
            takhte[0][1] = p1
            break
        input(f"{p2}, roll the dice:")
        y = dice()
        print(f"{p2}, dice rolled. you got {y}")
        if y != 6:
            print("sorry, next ones turn.")
        elif y == 6:
            print("you can enter the bord.")
            takhte[0][1] = p2
            break
elif p == p2:
    while True:
        input(f"{p2}, roll the dice:")
        y = dice()
        print(f"{p2}, dice rolled. you got {y}")
        if y != 6:
            print("sorry, next ones turn.")
        elif y == 6:
            print("you can enter the bord.")
            takhte[0][1] = p2
            break
        input(f"{p1}, roll the dice:")
        y = dice()
        print(f"{p1}, dice rolled. you got {y}")
        if y != 6:
            print("sorry, next ones turn.")
        elif y == 6:
            print("you can enter the bord.")
            takhte[0][1] = p1
            break
else:
    print("error, try again.")

print(takhte)

m = 0
n = 0
if takhte[0][1] == p1:
    while True:
        input(f"{p1}, roll the dice:")
        y = dice()
        print(f"{p1}, dice rolled. you got {y}")
        takhte[n][1] = " "
        n = n + y
        if n >= 20:
            print(f"{p1}, you win!")
            break
        takhte[n][1] = p1
        print(takhte)
        input(f"{p2}, roll the dice:")
        y = dice()
        print(f"{p2}, dice rolled. you got {y}")
        takhte[m][1] = " "
        m = m + y
        if m >= 20:
            print(f"{p2}, you win!")
            break
        takhte[m][1] = p2
        print(takhte)
        if m == n:
            print(f"{p1}, you got left out. Start over from square one.")
            n = 0
elif takhte[0][1] == p2:
    while True:
        input(f"{p2}, roll the dice:")
        y = dice()
        print(f"{p2}, dice rolled. you got {y}")
        takhte[m][1] = " "
        m = m + y
        if m >= 20:
            print(f"{p2}, you win!")
            break
        takhte[m][1] = p2
        print(takhte)
        input(f"{p1}, roll the dice:")
        y = dice()
        print(f"{p1}, dice rolled. you got {y}")
        takhte[n][1] = " "
        n = n + y
        if n >= 20:
            print(f"{p1}, you win!")
            break
        takhte[n][1] = p1
        print(takhte)
        if n == m:
            print(f"{p2}, you got left out. Start over from square one.")
            m = 0

print("END")