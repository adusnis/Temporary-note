from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/see', methods=['POST'])
def see():
    code = request.form['code']
    try:
        with open(f'{code}.txt', mode='r', encoding='utf-8') as f:
            text = f.read()
    except:
        return render_template('see.html', respond = "มีบางอย่างผิดพลาด")
    return render_template('see.html', code =  code, text = text)


@app.route("/", methods=['POST'])
def save():
    textinput = dict(request.form.items())
    input = textinput['input-field']
    code = ''.join(random.choices(string.ascii_letters, k=3))
    with open(f'{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{input}')
    return render_template('index.html', text = input, code = code)