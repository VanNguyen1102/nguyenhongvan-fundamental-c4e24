from random import randint

word_list = ["champion", "hexagon", "meticulous"]

i = randint(0, (len(word_list) - 1))
new = word_list[i]
characters = list(new)

for _ in range(len(characters)):
    n = randint (0, len(characters) - 1)
    ch = characters[n]
    print(ch, end =" ")
    characters.pop(n)

print()

user_guess = input("Your guess: ")
if user_guess == new:
    print("Hura")
else:
    print(":(")
