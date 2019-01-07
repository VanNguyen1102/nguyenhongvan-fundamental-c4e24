from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/database", methods=['GET', 'POST'])
def database():
    if request.method == 'POST':
        database = request.form
        return render_template("database.html", database=database)

if __name__ == "__main__":
    app.run(debug=True)

