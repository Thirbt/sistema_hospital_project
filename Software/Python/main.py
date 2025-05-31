'''
 * NOME: Nomes
 * DATA: 30/05/2025
 * PROJETO: Flask Web
 * VERSAO: 1.0.0
 * DESCRICAO: - feat: Criar página  de exemplos.
 * LINKS: 
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)