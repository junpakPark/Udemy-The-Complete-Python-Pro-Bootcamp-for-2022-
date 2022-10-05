from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_empahasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>This is a kitten</p>' \
        '<img src="https://media3.giphy.com/media/vLTY2ZfxrZ3gqx3W0k/giphy.gif?cid=ecf05e47snzi5snpxrzpbty1' \
        'f7kuvd7vhgk0tab2hu0ik0pj&rid=giphy.gif&ct=g" width="480">'


@app.route('/bye')
@make_bold
@make_empahasis
@make_underlined
def bye():
    return "Bye!!"


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello! {name}, Are you {number} years old?!"


if __name__ == "__main__":
    app.run(debug=True)
