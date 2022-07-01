import requests

#Get
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)
print(requisicao.json())

requisicao = requests.get('https://teste-a3b68-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.json())

#post
'''informacoes = '{"Nome": "iva"}'
requisicao = requests.post('https://teste-a3b68-default-rtdb.firebaseio.com/.json', data = informacoes)
print(requisicao)
print(requisicao.json())'''

#PATCH
informacoes = '{"Nome": "Maria", "Sobrenome": "Iva", "Idade": "52" }'
requisicao = requests.patch('https://teste-a3b68-default-rtdb.firebaseio.com/-N5qOktg-h8byZJIfGtw.json', data = informacoes)
print(requisicao)
print(requisicao.json())


