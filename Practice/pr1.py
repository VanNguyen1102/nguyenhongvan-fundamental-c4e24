from random import randint

n = randint(0,300)

while True:
    for i in range (5):
        i = int(input("Guess number: "))
        if i == n:
            print("Hura!")
        else:
            print(":(")
    break