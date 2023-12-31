# Decorator:
# -> a function that wraps another function and which provides additional functionality to the existing function

# Functions can have input/functionality/output
# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2

# function are first-class objects and can be passed around as argument eg:int/string/float etc.

# def calculate(calc_function, n1, n2):   # use calc_function to put one of the above function name
#     return calc_function(n1, n2)


# result = calculate(add, 9, 3)
# print(result)


# Functions can be nested in other functions
# def outer_function():
#     print("I am outer")

#     def nested_function():
#         print("I am inner")

#     nested_function()


# outer_function()

# Functions can be returned from other functions


# def outer_function():
#     print("I am outer")

#     def nested_function():
#         print("I am inner")

#     return nested_function

# inner_function = outer_function()   # prints "I am outer" after evaluating this line
# inner_function()    # prints "I am inner"


# Python Decorator Function
import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function()

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         # Do something after
#     return wrapper_function

# @delay_decorator
# the above line is same as:
# decorated_function = delay_decorator(say_hello)
# decorated_function()
# def say_hello():
#     print("Hello")

# def say_bye():
#     print("Bye")

# def say_greeting():
#     print("How are you?")


# say_greeting()

# Advanced python decorator functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Ram")
new_user.is_logged_in = True
create_blog_post(new_user)

