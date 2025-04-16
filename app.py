from flask import Flask, render_template, jsonify
from scraping import pegar_horoscopo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/horoscopo/<signo>')
def horoscopo(signo):
    resultado = pegar_horoscopo(signo)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
