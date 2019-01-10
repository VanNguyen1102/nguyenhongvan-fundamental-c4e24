from flask import Flask, render_template, request
from models.river import River
import mlab

mlab.connect()

app = Flask(__name__)

# Ex2
@app.route("/river/africa")
def africa_river():
    river_list = River.objects(continent="Africa")
    return render_template("africa_river.html", river_list=river_list)

# Ex3
@app.route("/river/samerica")
def samerica_river():
    river_list = River.objects(continent="S. America", length__lt=1000)
    return render_template("africa_river.html", river_list=river_list)

if __name__ == "__main__":
    app.run(debug=True)