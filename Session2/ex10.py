a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c
a2 = a * 2

if d < 0:
    print ("No solutions")
elif d == 0:
    print ("1 solution")
    x = (-b) / a2
    print ("x = ", x)
else:
    print ("2 solutions")
    d_sqrt = d ** 0.5
    x1 = (-b + d_sqrt) / a2
    print ("x1 = ", x1)
    x2 = (-b - d_sqrt) / a2
    print ("x2 = ", x2)
