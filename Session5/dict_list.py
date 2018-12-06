p1 = {
    "name": "H.Duc",
    "age": 25,
    "city": "Hai Phong"
}

p2 = {
    "name": "Huong",
    "age": 26,
    "city": "Hai Duong"
}

p3 = {
    "name": "Long",
    "age": 19,
    "city": "Ha Noi"
}

p_list = [
    {
    "name": "H.Duc",
    "age": 25,
    "city": "Hai Phong"
    },
    {
    "name": "Huong",
    "age": 26,
    "city": "Hai Duong"
    },
    {
    "name": "Long",
    "age": 19,
    "city": "Ha Noi"
    }
]

# p = p_list[0]
# print(p)
# print(p["name"])
# print(p["age"])

for p in p_list:
    print(p["name"])
    print(p["age"])
    print(p["city"])