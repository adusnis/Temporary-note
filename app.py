import os
from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)
# define the path of folder storing text files
# in this case, the path is root directory.

DATA_PATH = "/"

def createcode():
    code = ''.join(random.choices(string.ascii_letters, k=3))
    if f"{code}.txt" in os.listdir(DATA_PATH):
        # regenerate code
        # actually, it is recommended to prevent similar code since the code came from random.
        return createcode()
    return code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def see():
    textinput = dict(request.form.items())
    code = textinput['code']
    try:
        with open(f'data/{code}.txt', mode='r', encoding='utf-8') as f:
            text = f.read()
    except:
        return render_template('index.html', respond = "มีบางอย่างผิดพลาด ไม่พบข้อมูล")
    return render_template('see.html', code =  code, text = text)


@app.route("/create", methods=['POST'])
def create():
    code = createcode()
    text = request.form.get('input-field')
    with open(f'data/{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(text)
    print("มีคนมาใช้งานด้วยแหละแกร")
    return render_template('see.html', code=code, text=text)


@app.route("/<code>/upload", methods=['POST'])
def upload(code):
    text = request.form.get('input-field')
    with open(f'data/{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(text)
    return render_template('see.html', code=code, text=text)
    


@app.route('/<code>/update', methods=['POST'])
def update(code):
    try:
        with open(f'data/{code}.txt', mode='r', encoding='utf-8') as f:
            text = f.read()
    except:
        return render_template('see.html', respond="มีบางอย่างผิดพลาด ไม่พบข้อมูล", text=text)
    return render_template('see.html', code=code, text=text)

app.run(debug=True)