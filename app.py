# encoding=utf-8

from flask import Flask
from flask import render_template
from flask import request

from assembler import Assembler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', HELLO='hello')


@app.route('/content', methods=['POST'])
def content():
    data = request.form['data']
    ass = Assembler(data)
    ass.gen_bin_instructions()
    return ass.show_ins_table()


if __name__ == '__main__':
    app.run()