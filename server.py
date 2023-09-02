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

    response2 = requests.get(url=f"https://api.agify.io?name={name}").json()

    return render_template("guess.html", name=name.title(), gender=data["gender"], age=response2["age"])


if __name__ == "__main__":
    app.run(debug=True)
