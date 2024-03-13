from app import app
from flask import render_template

@app.route('/add/<num1>/<num2>')
def add_nums(num1, num2):
    operation = '+'
    result = int(num1)+int(num2)
    return render_template('results.html', num1=num1, num2=num2, operation=operation, result=result)

@app.route('/sub/<num1>/<num2>')
def sub_nums(num1, num2):
    operation = '-'
    result = int(num1)-int(num2)
    return render_template('results.html', num1=num1, num2=num2, operation=operation, result=result)

@app.route('/mult/<num1>/<num2>')
def mult_nums(num1, num2):
    operation = '*'
    result = int(num1)*int(num2)
    return render_template('results.html', num1=num1, num2=num2, operation=operation, result=result)

@app.route('/div/<num1>/<num2>')
def div_nums(num1, num2):
    try:
        operation = '/'
        result = int(num1)/int(num2)
        return render_template('results.html', num1=num1, num2=num2, operation=operation, result=result)
    except ZeroDivisionError:
        return f'<h1>Cannot divide by 0. Please replace second number.</h1>'
