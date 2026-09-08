#sang kaghaz ghachi

print("First person, make your choice.. Sang, Kaghaz, Ghachi?")

first = input()

print("Second person, make your choice.. Sang, Kaghaz, Ghachi?")

second = input()

if first == "sang" or first == "Sang":
    if second == "sang" or second == "Sang":
        print("It's a draw. Try again.")
    elif second == "kaghaz" or second == "Kaghaz":
        print("The second person is the winner.")
    elif second == "ghachi" or second == "Ghachi":
        print("The first person is the winner.")
    else :
        print("The response was unclear. Please try again.")
elif first == "kaghaz" or first == "Kaghaz":
    if second == "sang" or second == "Sang":
        print("The first person is the winner.")
    elif second == "kaghaz" or second == "Kaghaz":
        print("It's a draw. Try again.")
    elif second == "ghachi" or second == "Ghachi":
        print("The second person is the winner.")
    else :
        print("The response was unclear. Please try again.")
elif first == "ghachi" or first == "Ghachi":
    if second == "sang" or second == "Sang":
        print("The second person is the winner.")
    elif second == "kaghaz" or second == "Kaghaz":
        print("The first person is the winner.")
    elif second == "ghachi" or second == "Ghachi":
        print("It's a draw. Try again.")
    else :
        print("The response was unclear. Please try again.")
else :
    print("The response was unclear. Please try again.")