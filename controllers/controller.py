from app import app
from modules.calculator import add, subtract, multiply, divide
# from flask import render_template
# homework brief is ambiguous as to if we are to use an HTML page and render template to display the result


@app.route("/")
def say_hello():
    return "hello world! This is the homepage."

@app.route("/add/<number_1>/<number_2>")
def add_controller(number_1, number_2):
    return add(int(number_1), int(number_2))
  
@app.route("/subtract/<number_1>/<number_2>")
def subtract_controller(number_1, number_2):
    return subtract(int(number_1), int(number_2))
    
@app.route("/multiply/<number_1>/<number_2>")
def multiply_controller(number_1, number_2):
    return multiply(int(number_1), int(number_2))

@app.route("/divide/<number_1>/<number_2>")
def divide_controller(number_1, number_2):
    return divide(int(number_1), int(number_2))
