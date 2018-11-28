loop = True
while loop:
    pw = input("Your password? ")
    if len(pw) > 8:
        # so ky tu lon hon 8
        if (not pw.islower()) and (not pw.isupper()) and (not pw.isdigit()):
            # co ca chu va so, chu hoa va chu thuong
            loop = False

print ("Welcome")