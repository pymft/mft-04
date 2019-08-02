import sqlite3
import time
from flask import Flask,render_template, request

app = Flask('my application')



def write_into_file(name, w, h):
    conn = sqlite3.connect("../../a_note_on_relational_databases/bmi.sqlite")

    conn.execute(f"""INSERT INTO bmi (NAME, HEIGHT, WEIGHT) VALUES ('{name}', {h}, {w});""")
    conn.commit()

def get_data():
    conn = sqlite3.connect("../../a_note_on_relational_databases/bmi.sqlite")

    res = conn.execute("Select * from bmi")
    rows = list(res)

    return rows


@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        weight = float(request.form['w'])
        height = float(request.form['h'])
        name = request.form['name']
        bmi = weight / height ** 2
        bmi_preview = f"{bmi:.4f}"
        write_into_file(name, weight, height)
        rows = get_data()
        return render_template("index.html", bmi=bmi, bmi_preview=bmi_preview, rows=rows)


app.run(host="0.0.0.0", port=8088, debug=True)

