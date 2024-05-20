from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_inductance():
    if request.method == 'POST':
        number_of_turns = int(request.form.get('number_of_turns'))
        radius = float(request.form.get('radius'))
        length = float(request.form.get('length'))

        # Stała próżni
        mu_0 = 4 * 3.14159 * 10**-7

        # Obliczanie indukcyjności
        inductance = (mu_0 * (number_of_turns**2) * (3.14159 * (radius**2))) / length

        return render_template('result.html', inductance=inductance)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
