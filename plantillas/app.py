from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Inicio')
def index():
    return render_template('inicio.html')

@app.route('/Animales ')
def index():
    return render_template('animales.html')

@app.route('/Vehiculos')
def index():
    return render_template('vehiculos.html')

@app.route('/Maravillas')
def index():
    return render_template('maravillas.html')

@app.route('/Acerca')
def index():
    return render_template('acerca.html')

@app.route('/crearCuenta')
def crear_cuenta():
    return render_template('creacuenta.html')

if __name__=='__main__':
    app.run(debug=True)
