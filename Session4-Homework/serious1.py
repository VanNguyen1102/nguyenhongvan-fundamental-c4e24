items = ["T-shirt", "Sweater"]

while True:
    n = input("Welcome to our shop. What do you want (C, R, U, D)? ").upper()

    if n == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif n == "R":
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif n == "U":
        i = int(input("Update position: "))
        new_item = input("New item? ")
        items[i] = new_item
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif n == "D":
        d = int(input("Delete position: "))
        items.pop(d-1)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif n == "E":
        break
