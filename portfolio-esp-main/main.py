# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    # Variables por defecto (False)
    button_python = False
    button_discord = False
    button_html = False

    if request.method == 'POST':
        if 'button_python' in request.form:
            button_python = True
        elif 'button_discord' in request.form:
            button_discord = True
        elif 'button_html' in request.form:
            button_html = True

    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html
    )

if __name__ == "__main__":
    app.run(debug=True)
