from flask import Flask,render_template
import datetime
import requests



app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"https://api.genderize.io/?name={name}")
    data = response.json()
    return render_template("guess.html", name=data["name"], gender=data["gender"])


if __name__ == "__main__":
    app.run(debug=True)
