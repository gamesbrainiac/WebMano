# encoding=utf-8

from flask import Flask, jsonify
from flask import render_template
from flask import request

from assembler import Assembler
from computer import Computer
from storage import show_bin_rep

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/content', methods=['POST'])
def content():
    data = request.form['data']
    ass = Assembler(data)
    ass.gen_bin_instructions()
    c = Computer()
    program_start, end = ass.load(c.ram)
    c.run(program_start)
    return jsonify({
        'assembler': ass.show_ins_table(),
        'run': c.ram.show_relevant(program_start, end),
        'storage': show_bin_rep(data)
    })


if __name__ == '__main__':
    app.run()