from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
        except ValueError:
            result = "Invalid input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
