from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GBA')

lista = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['nome']
    console = request.form['console']
    jogo =Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['password']:
        return redirect('/')
    else:
        return  redirect('/login')

app.run(debug=True)