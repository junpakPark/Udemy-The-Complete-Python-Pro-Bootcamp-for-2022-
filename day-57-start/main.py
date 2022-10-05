from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    name
    age = requests.get(f"https://api.agify.io/?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog')
def get_blog():
    blog_list = requests.get("https://api.npoint.io/b5a96a93334b1044f6f8").json()
    return render_template("blog.html", blogs=blog_list)


if __name__ == "__main__":
    app.run(debug=True)


