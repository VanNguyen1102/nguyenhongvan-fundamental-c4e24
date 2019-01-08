from flask import Flask, render_template, request
from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()

app = Flask(__name__)

@app.route("/register")
def register():
        return render_template("register.html")

if __name__ == '__main__':
  app.run(debug=True)