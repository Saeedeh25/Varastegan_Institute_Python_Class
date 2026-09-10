# Two-digit prime numbers

y = 10

while y <= 99:
    z = 2
    while z <= y:
        x = y % z
        if x == 0:
            break
        else:
            z = z + 1
    if z == y:
        if y != 1:
            print(y)
    y = y + 1

print("end.")