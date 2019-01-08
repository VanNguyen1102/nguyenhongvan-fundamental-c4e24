from flask import Flask, render_template, request
from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()

class Register(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = IntField()

app = Flask(__name__)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']

        a = Register(name=name, email=email, username=username, password=password)
        a.save()
        
        return "Sucessful"

if __name__ == "__main__":
    app.run(debug=True)
