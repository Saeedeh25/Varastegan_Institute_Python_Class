x = True
numbers = []
while True:
    numbers.append(int(input("enter the number:")))
    c = input("do you want to enter an other?")
    if c.lower() == "no":
        break        

#for i in numbers:
#    print(i)

# miangin
x = 0
for i in numbers:
    x = i + x
mian = x /len(numbers)
print(f"miangin: {mian}")

#minimum
min = numbers[0]
for i in numbers:
    if min > i:
        min = i
    
print(f"minimum: {min}")

#maximum
max = numbers[0]
for i in numbers:
    if max < i:
        max = i
    
print(f"maximum: {max}")

#warians
x = 0
for i in numbers:
    x = (i - mian) ** 2 + x
war = x / len(numbers)

print(f"warians: {war}")

print("end")