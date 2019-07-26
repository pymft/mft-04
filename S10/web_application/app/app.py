from flask import Flask

app = Flask('my application')


@app.route('/')
def main_page():
    return "<h1>Hello</h1>"

app.run(host="0.0.0.0")
