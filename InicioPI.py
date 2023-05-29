from bd import *
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

# Amostras em memória (substitua por acesso a banco de dados real)
amostras = []

# Rota para obter a tabela de classificação


@app.route('/tabela', methods=['GET'])
def get_data():
    media = classificacao()
    media = jsonify({"tabela": media})
    return media

# Rota para obter a tabela de amostras


@app.route('/mostrar', methods=['GET'])
def get_data_amostras():
    amostras = printdados()
    amostras = jsonify({"mostrar": amostras})
    return amostras

# Rota para adicionar uma amostra


@app.route('/amostras', methods=['POST'])
def add_sample():
    co = request.json['co']
    so2 = request.json['so2']
    no2 = request.json['no2']
    o3 = request.json['o3']
    mp25 = request.json['mp25']
    mp10 = request.json['mp10']

    inseredados(float(co), float(so2), float(no2),
                float(o3), float(mp25), float(mp10))

    return jsonify({"message": "Amostra adicionada com sucesso"})

# Rota para atualizar uma amostra


@app.route('/amostras/<id>', methods=['PUT'])
def update_sample(id):
    co = request.json['co']
    so2 = request.json['so2']
    no2 = request.json['no2']
    o3 = request.json['o3']
    mp25 = request.json['mp25']
    mp10 = request.json['mp10']

    alteradados(int(id), float(co), float(so2), float(no2),
                float(o3), float(mp25), float(mp10))

    return jsonify({"message": "Amostra atualizada com sucesso"})


# Rota para excluir uma amostra


@app.route('/amostras/<id>', methods=['DELETE'])
def delete_sample(id):
    deletadados(id)
    return jsonify({"message": "Amostra deletada com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)

""" if Mp10 > 250 and Mp25 > 125 and O2 > 200 and cO > 15 and No2 > 1130 and So2 > 800:
    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')

elif Mp10 > 150 and Mp10 < 250 and Mp25 > 75 and Mp25 < 125 and O2 > 160 and O2 < 200 and cO > 13 and cO < 15 and No2 > 320 and No2 < 1130 and So2 > 365 and So2 < 800:
    print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')

elif Mp10 > 100 and Mp10 < 150 and Mp25 > 50 and Mp25 < 75 and O2 > 130 and O2 < 160 and cO > 11 and cO < 13 and No2 > 240 and No2 < 320 and So2 > 40 and So2 < 365:
    print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Pode ocasionar também em efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')

elif Mp10 > 50 and Mp10 < 100 and Mp25 > 25 and Mp25 < 50 and O2 > 100 and O2 < 130 and cO > 9 and cO < 11 and No2 > 200 and No2 < 240 and So2 > 20 and So2 < 40:
    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')

media = classificacao()
MediaCalculo(media[0], media[1], media[2], media[3], media[4], media[5])

print("A média do MP10 é ", media[0], "\n")
print("A média do MP25 é ", media[1], "\n")
print("A média do O3 é ", media[2], "\n")
print("A média do CO é ", media[3], "\n")
print("A média do NO2 é ", media[4], "\n")
print("A média do SO2 é ", media[5], "\n") """
