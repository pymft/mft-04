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

        return render_template("index.html", javab=bmi)



app.run(host="0.0.0.0")
