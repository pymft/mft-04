from flask import Flask,render_template, request

app = Flask('my application')


@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        weight = float(request.form['w'])
        height = float(request.form['h'])
        bmi = weight / height ** 2
        bmi_preview = f"{bmi:.2f}"

        return render_template("index.html", bmi=bmi, bmi_preview=bmi_preview)


app.run(host="0.0.0.0")

