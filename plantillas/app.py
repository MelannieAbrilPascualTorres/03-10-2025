from flask import Flask, render_template, request, redirect, url_for, flash

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_dificil_de_adivinar'

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/formulario')
def crear_cuenta():
    return render_template('formulario.html')

@app.route('/registrando')
def registram():
    return ""
@app.route('/registrando', methdod = ("GET", "POST"))
def registrame():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        dia = request.form["dia"]
        mes = request.form["mes"]
        año = request.form["año"]
        genero = request.form["mujer"]
        genero = request.form["hombre"]
        genero = request.form["otro"]
        cuenta = request.form["cuenta"]
        contra = request.form["contra"]

@app.route('/sesion')
def iniciar_sesion():
    return render_template('sesion.html')

if __name__=='__main__':
    app.run(debug=True)
