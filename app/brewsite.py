from flask import Flask, render_template
from flask import render_template as rt


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", username="Amber")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", username="Amber")

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", username="Amber")

@app.route("/about")
def about():
    return rt("about.html", username="Amber")

if __name__ == "__main__":
    app.run(debug=True)