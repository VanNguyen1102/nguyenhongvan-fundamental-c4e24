from flask import Flask, render_template, request
import mlab

mlab.connect()

app = Flask(__name__)

@app.route("/search", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("project.html")
    elif render_template == 'POST':
        form = request.form
        food_name = form['food_name']
        location = form['location']
        rate = form['rate']
        new_food = Food(food_name=food_name, location=location, rate=rate)
        new_food.save()
        return "Done"

if __name__ == "__main__":
    app.run(debug=True)
