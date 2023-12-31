# Variable rules:
# -> add variables section to a URL by marking section with <variable_name>
# -> the function then receives the <variable_name> as a keyword argument
# -> use a converter to specify the type of the argument like <converter:variable_name>

# Converter types:

# 1.string-(default) accepts any text without a slash
# 2.int-accepts positive integers
# 3.float-accepts positive floating point values
# 4.path-like string but also accepts slashes
# 5.uuid-accepts UUID strings

# * if debug support enabled the server will reload itself on the code changes

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper


# different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye"

# creating variable path and converting the path to the specified data type
# @app.route("/username/<user>")  # here <user> is the variable
# def greet(user):
#     return f"hello you {user}"


@app.route("/username/<user>/<int:number>")  # here <user> and <number> with int type are two variables
def greet(user, number):
    return f"hello you {user}, you're {number} years old"


if __name__ == "__main__":
    # run app in debug mode to auto-reload
    app.run(debug=True)


