from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def load_home():
    return render_template('index.html')

@app.route('/bmi/')
def calculate_bmi():
    weight = float(request.args.get('weight'))
    height = float(request.args.get('height'))

    if weight <= 0 or height <= 0:
        return render_template('index.html', error='Please enter valid weight and height (must be greater than 0).')

    bmi = weight / (height / 100) ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 25:
        category = 'Normal weight'
    elif bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obese'

    return render_template('result.html', bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
