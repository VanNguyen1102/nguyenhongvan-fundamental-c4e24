inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#1
inventory["pocket"] = []

#2
inventory["pocket"] = ["seashell", "strange berry", "lint"]

#3
del(inventory["backpack"][1])

#4
inventory["gold"] += 50

print(inventory)