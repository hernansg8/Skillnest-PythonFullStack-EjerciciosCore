#########################
#|  PYTHON FULL STACK   |
#| CORE 8               |
#| Hernán Soto          |
#########################

from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "eljuegodeldestino"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    #Obtener datos del request:
    session['nombre'] = request.form['nombre']
    session['lugar'] =request.form['lugar']
    session['numero'] = int(request.form['numero'])
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']

    #Redireccionamiento aleatorio:
    if random.randint(0,1) > 0:
        #Redireccionar:
        return redirect(
            "/futuro"
        )
    else:
        #Redireccionar:
        return redirect(
            "/malasuerte"
        )

@app.route('/futuro')
def futuro():
    return render_template("futuro.html")

@app.route('/malasuerte')
def malasuerte():
    return render_template("malasuerte.html")

if __name__=="__main__":   
    app.run(debug=True) 