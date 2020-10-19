import os
import json
from flask import Flask, render_template
from file_check import file_abs_path as path
from file_check import file_exists_check as exist

app = Flask(__name__)

def read_data():
    filename= 'menu.json'
    if exist(filename):
        with open(path() + filename, 'r') as fr:
            menu = json.load(fr)
            return dict(menu)
    else:
        print('somthing wrong!')
        return False

@app.route('/')
def index():
    menu = read_data()
    if menu:
        return render_template('index.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
