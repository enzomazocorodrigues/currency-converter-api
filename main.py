from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"

@app.route("/convertemoeda", methods=['GET'])
def convertemoeda():
    valor = float(request.args.get("valor"))
    if not valor: abort(400, 'Valor deve ser informado.')
    response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
    if not response.status_code == 200: abort(500, 'Não foi possível converter as moedas')
    data = response.json()
    cotacao_usd =  float(data['USDBRL']['bid'])
    cotacao_eur =  float(data['EURBRL']['bid'])
    usd = valor * cotacao_usd
    eur = valor * cotacao_eur
    result = { 'real': valor, 'dolar': usd, 'euro': eur }
    return jsonify(result)

if __name__ == "__main__":
    app.run()