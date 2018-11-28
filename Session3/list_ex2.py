
places = ["Ha Noi", "Da Nang", "Sai Gon"]
print(*places, sep=", ")

i = int(input("Choose one place: "))
if i >= len(places):
    print("error")
else:
    print(places[i])
