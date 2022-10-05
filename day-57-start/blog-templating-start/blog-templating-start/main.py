from flask import Flask, render_template
from post import Post
import requests


posts = requests.get("https://api.npoint.io/b5a96a93334b1044f6f8").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def post_list():
    return render_template("index.html", posts=post_objects)


@app.route('/blog/<int:index>')
def post_detail(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
