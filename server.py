from flask import Flask, render_template
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


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
