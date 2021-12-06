from os import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Queen Silvia"
    letters = list(name)
    return render_template('basic.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
