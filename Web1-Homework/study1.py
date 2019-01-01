from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    infor = {
        "name": "Nguyen Hong Van",
        "job": "staff",
        "company": "CVN",
        "hobbies": "reading books"
    }
    return render_template("about-me.html", me = infor)

@app.route("/school")
def school():
    return redirect("https://techkids.vn/")

if __name__ == "__main__":
    app.run(debug=True)