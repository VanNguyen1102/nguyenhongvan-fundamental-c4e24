h = float(input("Enter your height (cm): "))
w = float(input("Enter your weight (kg): "))
h = h * 0.01

BMI = w / (h * h)
print ("Your BMI is ",BMI)

if BMI < 16:
    print("Severely underweight")

elif BMI < 18.5:
    print("Underweight")

elif BMI < 25:
    print("Normal")

elif BMI < 30:
    print("Overweight")

else:
    print("Obese")