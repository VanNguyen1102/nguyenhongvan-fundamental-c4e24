# 2.1
print("Hello, my name is Van and these are my ship sizes")
sizes = [5, 7, 300, 90, 24, 50, 75]
print(sizes)

# 2.2
n = max(sizes)
print("Now my biggest ship has size", n, "let's shear it")

# 2.3
print("After shearing, here is my flock")
index = sizes.index(n)
sizes[index] = 8
print(sizes)

# 2.4
print("One month has passed, now here is my flock")
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print(sizes)
