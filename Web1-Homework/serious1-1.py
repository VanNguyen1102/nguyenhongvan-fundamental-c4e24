from flask import Flask

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    BMI = weight/((height/100)**2)
    if BMI < 16:
        return("Your BMI is " + str(BMI) + " Severely underweight")
    elif BMI < 18.5:
        return("Your BMI is " + str(BMI) + " Underweight")
    elif BMI < 25:
        return("Your BMI is " + str(BMI) + " Normal")
    elif BMI < 30:
        return("Your BMI is " + str(BMI) + " Overweight")
    else:
        return("Your BMI is " + str(BMI) + "Obese")

if __name__ == "__main__":
    app.run(debug=True)
