from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    users = {
        "Van": {
            "name": "Van",
            "age": 26,
            "job": "engineer",
            "hobbies": "books"
        },
        "Thanh": {
            "name": "Thanh",
            "age": 27,
            "job": "staff",
            "hobbies": "K-dramas"
        }
    }
    return render_template("user.html", users = users, username = username)

if __name__ == "__main__":
    app.run(debug=True)