#########################
#|  PYTHON FULL STACK   |
#| CORE 7               |
#| Hernán Soto          |
#########################

from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "Aqui usar una palabra clave"

contador = 0

@app.route('/')
def index():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 0

    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template(
        "index.html",
        visitas = session['visitas'],
        reinicios = session['reinicios']
    )

@app.route('/destruir_sesion')
def destruir():
    session.clear()
    return redirect('/')

@app.route('/aumentar', methods=['POST'])
def aumentar():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 0

    return redirect('/')

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    session.pop('visitas')
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 0

    return redirect('/')

@app.route('/aumentarCantidad', methods=['POST'])
def aumentarCantidad():
    session['visitas'] += int(request.form['cantidad'])-1
    return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)