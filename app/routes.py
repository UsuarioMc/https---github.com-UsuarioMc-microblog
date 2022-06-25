from app import app
from flask import render_template

# rota index
@app.route('/')
@app.route('/index')
# função da pagina Home ====================================
def index():
    nome = 'Miro Campos'
    dados = {'profissao': 'Design Gráfico', 'canal': 'Portfólio Miro'}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    titulo = 'Contato'
    return render_template('contato.html', titulo=titulo)