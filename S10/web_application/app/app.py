from flask import Flask,render_template

app = Flask('my application')


@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/dashboard')
@app.route('/dashboard/<user>/<int:rep>')
def dashboard_page(user="None", rep=1):
    return render_template("dashboard.html",
                           username=user, rep=rep)


app.run(host="0.0.0.0")
