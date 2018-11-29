from random import randint
n = randint(1, 100)

while True:
    i = int(input("Guess my number (1-100)? "))
    if i < n:
        print("Too small :(")
    elif i > n:
        print("A little too large :(")
    else:
        print("Bingo")
        break