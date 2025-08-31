"""A Flask web server to provide basic mathematical operations."""

from typing import Tuple, Union
from Maths.mathematics import summation, subtraction, multiplication
from flask import Flask, render_template, request

# It's good practice to use __name__ which helps Flask locate templates and static files.
app = Flask(__name__)

@app.route("/sum")
def sum_route() -> str:
    """Endpoint to calculate the sum of two numbers."""
    num1_str = request.args.get('num1')
    num2_str = request.args.get('num2')
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = summation(num1, num2)
        if result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)
        return render_template('index.html', result=result_str, num1=num1_str, num2=num2_str)
    except (TypeError, ValueError):
        error = "Error: Please provide two valid numbers for the operation."
        return render_template('index.html', error=error, num1=num1_str, num2=num2_str), 400

@app.route("/sub")
def sub_route() -> str:
    """Endpoint to calculate the difference of two numbers."""
    num1_str = request.args.get('num1')
    num2_str = request.args.get('num2')
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = subtraction(num1, num2)
        if result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)
        return render_template('index.html', result=result_str, num1=num1_str, num2=num2_str)
    except (TypeError, ValueError):
        error = "Error: Please provide two valid numbers for the operation."
        return render_template('index.html', error=error, num1=num1_str, num2=num2_str), 400

@app.route("/mul")
def mul_route() -> str:
    """Endpoint to calculate the product of two numbers."""
    num1_str = request.args.get('num1')
    num2_str = request.args.get('num2')
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = multiplication(num1, num2)
        if result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)
        return render_template('index.html', result=result_str, num1=num1_str, num2=num2_str)
    except (TypeError, ValueError):
        error = "Error: Please provide two valid numbers for the operation."
        return render_template('index.html', error=error, num1=num1_str, num2=num2_str), 400

@app.route("/")
def render_index_page() -> str:
    """Renders the main index page."""
    # This will look for a file named 'index.html' in a 'templates' folder
    # at the same level as server.py.
    return render_template('index.html')

if __name__ == "__main__":
    # Using debug=True is helpful for development as it provides better error
    # pages and reloads the server on code changes.
    app.run(host="0.0.0.0", port=8080, debug=True)
