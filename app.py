from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)

def createcode():
    code = ''.join(random.choices(string.ascii_letters, k=3))
    try:
        with open(f'{code}.txt', mode='r', encoding='utf-8') as f:
            f.read()
    except IOError:
        return code
    else:
        return createcode()


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
        return render_template('index.html', respond = "มีบางอย่างผิดพลาด ไม่พบข้อมูล")
    return render_template('see.html', code =  code, text = text)


@app.route("/create", methods=['POST'])
def create():
    code = createcode()
    text = request.form.get('input-field')
    with open(f'{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(text)
    return render_template('see.html', code=code, text=text)


@app.route("/<code>/upload", methods=['POST'])
def upload(code):
    text = request.form.get('input-field')
    print('1'+text)
    with open(f'{code}.txt', mode='w', encoding='utf-8') as f:
        f.write(text)
    print('2'+text)
    return render_template('see.html', code=code, text=text)


@app.route('/<code>/update', methods=['POST'])
def update(code):
    try:
        with open(f'{code}.txt', mode='r', encoding='utf-8') as f:
            text = f.read()
    except:
        return render_template('see.html', respond="มีบางอย่างผิดพลาด ไม่พบข้อมูล", text=text)
    print(text)
    return render_template('see.html', code=code, text=text)

app.run(debug=True)