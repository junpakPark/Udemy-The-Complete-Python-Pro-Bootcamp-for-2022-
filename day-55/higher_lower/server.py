from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>choose 0- 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200">'


@app.route('/<int:number>')
def cnumber_choice(number):
    if number < 6:
        return f'<h1 style="color: red">{number} is too low.. Try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="200">'
    elif number > 6:
        return f'<h1 style="color: blue">{number} is too high.. Try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="200">'
    else:
        return f'<h1 style="color: green">Yes. {number} is the answer! You found it!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="200">'


if __name__ == "__main__":
    app.run(debug=True)
