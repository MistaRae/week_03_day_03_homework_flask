from app import app


@app.route("/")
def say_hello():
    return "hello world! This is the homepage."

@app.route("/add/<number1>/<number2>")
def add(number1, number2):
    number_1 = int(number1)
    number_2 = int(number2)
    sum = number_1 + number_2
    return f"The answer is {sum}"
   

@app.route("/subtract/<number1>/<number2>")
def subtract(number1, number2):
    number_1 = int(number1)
    number_2 = int(number2)
    difference = number_1 - number_2
    return f"The answer is {difference}"

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    number_1 = int(number1)
    number_2 = int(number2)
    product = number_1 * number_2
    return f"The answer is {product}"

@app.route("/divide/<number1>/<number2>")
def divide(number1, number2):
    number_1 = int(number1)
    number_2 = int(number2)
    quotient = number_1 / number_2
    return f"The answer is {quotient}"