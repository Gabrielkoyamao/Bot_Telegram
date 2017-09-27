from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   


app = Flask(__name__)


@app.route('/api/v1/filmes', methods=['GET'])
def filmes2():
    
    return "Tudo pronto!"


if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5002))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='127.0.0.1', port=port)

