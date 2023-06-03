from bd import *
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

# Amostras em memória (substitua por acesso a banco de dados real)
amostras = []

# qualidade do AR


def Arqualiti(mp10, mp25, o3, co, no2, so2):

    if (mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800):
        return 'Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
    elif (mp10 > 150 or mp25 > 75 or o3 > 160 or co > 13 or no2 > 320 or so2 > 365):
        return 'Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.'
    elif (mp10 > 100 or mp25 > 50 or o3 > 130 or co > 11 or no2 > 240 or so2 > 40):
        return 'Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Pode ocasionar também em efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
    elif (mp10 > 50 or mp25 > 25 or o3 > 100 or co > 9 or no2 > 200 or so2 > 20):
        return 'Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
    else:
        return 'A qualidade do ar está boa.'


# Rota para obter a tabela de classificação
@app.route('/classificacao', methods=['GET'])
def get_data():
    media = classificacao()
    res = Arqualiti(media[0], media[1], media[2], media[3], media[4], media[5])
    media = jsonify({"classificacao": media, "mensagem": res})
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
