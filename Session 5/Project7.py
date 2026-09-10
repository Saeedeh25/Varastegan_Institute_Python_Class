# Three-digit numbers divisible by 3 and 5

i = 100

while i <= 999:
    y = i % 3
    z = i % 5
    if y == 0 and z == 0:
        print(i)
    i = i + 1

print("end.")