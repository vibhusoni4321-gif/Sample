```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""

    if request.method == 'POST':
        try:
            # Get form data
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation')

            # Perform operation
            if operation == 'add':
                result = num1 + num2

            elif operation == 'subtract':
                result = num1 - num2

            elif operation == 'multiply':
                result = num1 * num2

            elif operation == 'divide':
                if num2 == 0:
                    result = "Error: Cannot divide by zero"
                else:
                    result = num1 / num2

            else:
                result = "Invalid Operation"

        except ValueError:
            result = "Invalid Input"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
```
