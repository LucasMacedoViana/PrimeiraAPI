import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


# construir a funcionalidade
@app.route('/')
def homepage():
    return 'A API esta no ar'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('12-18 - Criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


# rodar a nossa api
app.run(host='0.0.0.0')
