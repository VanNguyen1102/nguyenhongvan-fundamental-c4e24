#1 read file => string
f = open("data.json")
text = f.read()

#2 load, parse, str => dict
import json
word = json.loads(text)

word = {
    "dog": "chó",
    "cat": "mèo",
    "pig": "heo",
}

while True:
    print(*word)
    n = input("Your word: ")
    if n in word:
        print(word[n])
        print()

        update = input("Do you want to update (Y/N)? ").upper()
        if update == "Y":
            new_translation = input("Your translation? ")
            word[n] = new_translation
            print("Done")
    else:
        print("Not found")
        add = input("Do you want to add (Y/N)? ").upper()
        if add == "Y":
            new_word = input("New translation? ")
            word[n] = new_word
            print(word)
