from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = ''
    category = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = round(weight / (height * height), 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi <= 22.9:
            category = "Normal weight"
        elif bmi >= 30:
            category = "Obese"
        else:
            category = "Overweight"

    return render_template('calcu.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)