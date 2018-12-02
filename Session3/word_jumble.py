from random import randint

word = "hexagon"
characters = list(word)

for _ in range (len(characters)):
# 1. Select character randomly
# 1.1. Random => number 0 => len -1 
# 1.2. number => index
    i = randint (0, len(characters) - 1)
    ch = characters[i]

# 2. Print selected characters
    print(ch, end=" ")

# 3. Remove
    characters.pop(i)
# print(characters)

print()

user_guess = input("Your guess: ")
if user_guess == word:
    print("Hura")
else:
    print(":(")
