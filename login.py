from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            erro = 'Usuário ou Senha errados. Tente novamente.'
        else:
            return redirect(url_for('interface'))
    return render_template('login.html', erro=erro)

@app.route('/interface')
def interface():
    return render_template('interface.html')  # render a template