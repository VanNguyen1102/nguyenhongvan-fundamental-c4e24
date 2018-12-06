print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3)? ")

answers = [35, 36, 40, 44]

for i in range (len(answers)):
    print(i + 1, answers[i], sep=". " )

user_choice = int(input("Your choice: "))
if user_choice == 4:
    print("Bingo")
else:
    print(":(")