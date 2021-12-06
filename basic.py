from os import name
from flask import Flask, render_template
import json as js
app = Flask(__name__)

def get_new_monarchs():
    with open('new_monarchs.json', 'r') as file:
        monarchs = js.load(file)
    return monarchs


@app.route('/')
def index():
    monarchs = get_new_monarchs()
    name1 = monarchs["Name"]
    name2 = monarchs["Marriage"]
    
    return render_template('basic.html', name1 = name1, name2 = name2)

if __name__ == '__main__':
    app.run(debug=True)
