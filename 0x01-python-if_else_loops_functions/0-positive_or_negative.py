#!/urs/bin/python3
mport random
number = random.randint(-10, 10)
print(f"{number}", end=" ")
if number > 0:
    print("is positive")
elif number < 0:
    print("is negative")
else:
    print("is zero")
