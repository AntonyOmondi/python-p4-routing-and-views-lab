#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f"{parameter}")
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = "\n".join(str(num) for num in range(parameter)) + "\n"
    return result

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == "div":
        if num2 == 0:
            return "Invalid Operation!", 400
        else:
            result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        return "Invalid Operation!", 400
    
    return str(result), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
