from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import telepot
import os


app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
    soup = BeautifulSoup(html_doc, "html.parser")


    data = []
    for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf hred"):
        nomeObj = dataBox.find("h2", class_="meta-title")
        imgObj = dataBox.find(class_="thumbnail ")
        sinopseObj = dataBox.find("div", class_="synopsis")
        dataObj = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")

        data.append({ 'nome': nomeObj.text.strip(),
                        'poster' : imgObj.img['data-src'].strip(),
                        'sinopse' : sinopseObj.text.strip(),
                        'data' :  dataObj.text[1:23].strip().replace('/',' ')})
                
    return jsonify({'filmes': data})

if __name__ == '__main__':
  
