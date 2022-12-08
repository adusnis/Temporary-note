from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/join', methods=['POST'])
def see():
    textinput = dict(request.form.items())
    code = textinput['code']
    try:
        with open(f'{code}.txt', mode='r', encoding='utf-8') as f:
            text = f.read()
    except:
        return render_template('index.html', respond = "มีบางอย่างผิดพลาด")
    return render_template('see.html', code =  code, text = text)


@app.route("/create", methods=['POST'])
def save():
    textinput = dict(request.form.items())
    text = textinput['input-field']
    code = ''.join(random.choices(string.ascii_letters, k=3))
    with open(f'{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{text}')
    return render_template('see.html', code=code, text=text)

'''
@app.route("/update", methods=['POST'])
def update():
    textinput = dict(request.form.items())
    text = textinput['input-field']
    code = textinput['code']
    with open(f'{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{text}')
    return render_template('see.html', code=code, text=text)
'''
#app.run(debug=True)