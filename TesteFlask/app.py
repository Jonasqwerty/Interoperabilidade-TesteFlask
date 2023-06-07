from flask import Flask, request, json

app = Flask(__name__, template_folder='.')

@app.route('/teste', methods=['GET'])
def teste ():
    return 'sucesso no teste'

@app.route('/soma', methods=['POST'])
def soma ():
    data = request.get_data()
    obj = json.loads( data )
    v1 = obj['v1']
    v2 = obj['v2']
    soma = v1 + v2
    obj = { "resultado" : soma }
    data = json.dumps( obj )
    return data

@app.route('/subtracao', methods=['POST'])
def subtracao ():
    data = request.get_data()
    obj = json.loads(data)
    subtracao = obj['v1'] - obj['v2']
    obj = {"resultado" : subtracao}
    data = json.dumps(obj)
    return data

@app.route('/divisao', methods=['POST'])
def divisao ():
    data = request.get_data()
    obj = json.loads(data)
    divisao = obj['v1'] / obj['v2']
    obj = {"resultado" : divisao}
    data = json.dumps(obj)
    return data

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao ():
    data = request.get_data()
    obj = json.loads(data)
    v1 = obj['v1']
    v2 = obj['v2']
    multiplicacao = v1 * v2
    obj = {"resultado" : multiplicacao}
    data =json.dumps(obj)
    return data

app.run(port=8085, use_reloader=True)