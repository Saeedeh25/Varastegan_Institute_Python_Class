x = True
numbers = []
while True:
    numbers.append(int(input("enter the number:")))
    c = input("do you want to enter an other?")
    if c.lower() == "no":
        break        

# miangin
x = 0
y = 0
min = numbers[0]
max = numbers[0]
for i in numbers:
    x = i + x
    if min > i:
        min = i
    if max < i:
        max = i
mian = x /len(numbers)

for i in numbers:
    y = (i - mian) ** 2 + y
war = y / len(numbers)

print(f"miangin: {mian}")
print(f"minimum: {min}")
print(f"maximum: {max}")
print(f"warians: {war}")

print("end")