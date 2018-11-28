while True:
    yob_str = input("Your year of birth? ")
    if yob_str.isdigit():
        break

yob = int(yob_str)
age = 2018 - yob
print (age)