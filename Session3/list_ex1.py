
favs = ["Chocolate", "Book", "Game"]
print("Hi, your things: ")
print(*favs, sep=", ") # thêm (*): tách từng phần tử (bỏ ngoặc)
                       # thêm sep (seperator): cách nhau bởi dấu phẩy

new_fav = input("Add one more favorite thing? ")
favs.append(new_fav)
print(*favs, sep=", ")
