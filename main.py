from flask import Flask
import random

app = Flask(__name__)

random_number_list = [i for i in range(1, 10)]
random_no = random.choice(random_number_list)


@app.route("/")
def guess_no_home():
    return '<h1> Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width = 200>'


def random_number(function):
    def wrapper(**args):
        if int(args['number']) < random_no:
            return function(args['number'], 'Low')
        elif int(args['number']) > random_no:
            return function(args['number'], 'High')
        else:
            return function(args['number'], 'correct')

    return wrapper


@app.route("/<number>")
@random_number
def guess_number(number, result):
    if result == 'correct':
        return "<b>You found me!<b></br>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width = 200>"
    elif result == 'High':
        return f"<b>Too {result}, try again!</b></br>" \
               f"<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width = 200>"
    else:
        return f"<b>Too {result}, try again!</b></br>" \
               f"<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width = 200>"


if __name__ == '__main__':
    app.run(debug=True)
