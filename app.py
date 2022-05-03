from flask import Flask, jsonify, request
import json

app = Flask(__name__)

colaboradores = [
    {'nome': 'Renan',
     'cargo': 'Analista',
     'habilidades': ['Python', 'C#']}
    ,
    {'nome': 'Matheus',
     'cargo': 'Analista',
     'habilidades': ['Ruby', 'Elixir']}
]


@app.route('/colaboradores/<int:id>/', methods=['GET', 'PUT'])
def colaborador(id):
    if request.method == 'GET':
        colaborador = colaboradores[id]
        return jsonify(colaborador)

# put nos dados
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        posicao = len(colaboradores)
        dados['id'] = posicao
        colaboradores.append(dados)
        return jsonify(colaboradores[posicao])

# todos os desenvolvedores
    elif request.method == 'GET':
        return jsonify(colaboradores)






if __name__ == '__main__':
        app.run(debug=True)