from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return ("<h1>Guess a number between 0 and 9:</h1>"
            "<img src='https://media.giphy.com/media/DhiRqIsofVMi7fWNBQ/giphy.gif'>")


random_number = random.randint(0, 9)

@app.route("/<int:number>")
def check(number):
    if number > random_number:
        return ('<h1 style="color:red;">Number is too high</h1>'
                '<img src="https://media.giphy.com/media/Y0ONIkhEuujDFvvY4Q/giphy.gif">')

    elif number < random_number:
        return ('<h1 style="color:orange;">Number is too low</h1>'
                '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif">')

    else:
        return ('<h1 style="color:green;">Correct Guess</h1>'
                '<img src="https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)




