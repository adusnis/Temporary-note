from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    f = open("note.txt", "r")
    text = f.read()
    return render_template('index.html',note = text)

@app.route("/", methods=['POST'])
def save():
    textinput = dict(request.form.items())
    input = textinput['inputsave']
    with open("note.txt", mode='w', encoding='utf-8') as f:
        f.write(f'{input}')
    return render_template('index.html', note = input)

