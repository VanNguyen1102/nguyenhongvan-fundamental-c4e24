n = input("What do you want? ")
items = ["dog", "cat", "chicken", "pig"]

if n == "C":
    new_item = input("What do you want to create? ")
    items.append(new)
    print(items)
elif n == "R":
    for index, item in enumerate(items):
    print(index + 1, item, sep=". ")
elif n == "U":
    new_value = input("What do you want to update? ")
    i  = int(input("In which position: "))
    items[i] = new_value
    print(items)
elif n == "D":
    d = int(input("What do you want to delete? "))
    items.pop(d)
    print(items)
