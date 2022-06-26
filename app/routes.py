from app import app
from flask import render_template

# rota index
@app.route('/')
@app.route('/index', defaults={'nome':'Usuário'})
@app.route('/index/<nome>/<profissao>/<canal>')

# função daS paginas ====================================
def index(nome, profissao, canal):
    dados = {'profissao': profissao, 'canal': canal}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    titulo = 'Contato'
    return render_template('contato.html', titulo=titulo)