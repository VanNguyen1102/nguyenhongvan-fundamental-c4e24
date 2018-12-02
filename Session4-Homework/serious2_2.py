# 2.5
print("Hello, my name is Van and these are my ship sizes")
sizes = [5, 7, 300, 90, 24, 50, 75]
print(sizes)

m = int(input("Enter the number of month: "))
for i in range (1, m+1):
    print("MONTH", i, end="")
    print()
    
    for j in range (len(sizes)):
        sizes[j] = sizes[j] + 50
    print("One month has passed, now here is my flock")
    print(sizes)

    n = max(sizes)
    print("Now my biggest ship has size", n, "let's shear it")

    print("After shearing, here is my flock")
    index = sizes.index(n)
    sizes[index] = 8
    print(sizes)

# 2.6
total = sum(sizes)
print("My flock has size in total:", total)
money = total * 2
print("I would get ", total, end=(" * 2$ = "))
print(money,"$")