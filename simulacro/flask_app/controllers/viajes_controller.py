from flask import render_template, redirect, request,session
from flask_app import app
from flask_app.models.viajes_model import Viaje
from flask_app.models.viajeros_model import Viajero
from datetime import date

@app.route('/dashboard')
def dashboard():
    viajes = Viaje.get_all()
    return render_template('dashboard.html', viajes = viajes)

@app.route('/nuevo')
def nuevo():
    print(f"ID: {session['id_usuario']}")
    return render_template('nuevo_viaje.html')

@app.route('/nuevo/save', methods=['POST'])
def crear_viaje():
    if date.fromisoformat(request.form['fecha_inicio']) < date.today():
        print('Error: la fecha de inicio debe ser mayor a la actual.')
    elif request.form['fecha_inicio'] > request.form['fecha_fin']:
        print('Error: la fecha de termino tiene que ser mayor a la fecha de inicio.')
    else:
        data = {
            "destino": request.form['destino'],
            "fecha_inicio": request.form['fecha_inicio'],
            "fecha_fin": request.form['fecha_fin'],
            "itinerario": request.form['itinerario'],
            "organizador": request.form['organizador']
        }
        Viaje.save(data)
    return redirect('/dashboard')

@app.route('/editar/<int:id>')
def editar(id):
    data={
        "id": id
    }
    viaje = Viaje.get_one(data)
    return render_template("editar_viaje.html", viaje = viaje)

@app.route('/editar/save', methods=['POST'])
def editar_viaje():
    if date.fromisoformat(request.form['fecha_inicio']) < date.today():
        print('Error: la fecha de inicio debe ser mayor a la actual.')
    elif request.form['fecha_inicio'] > request.form['fecha_fin']:
        print('Error: la fecha de termino tiene que ser mayor a la fecha de inicio.')
    else:
        data = {
            "id": request.form['id'],
            "destino": request.form['destino'],
            "fecha_inicio": request.form['fecha_inicio'],
            "fecha_fin": request.form['fecha_fin'],
            "itinerario": request.form['itinerario'],
            "organizador": request.form['organizador']
        }
        Viaje.update(data)
    return redirect('/dashboard')

@app.route("/dashboard/borrar/<int:id>")
def usuario_delete(id):
   data={
      "id": id
   }
   Viaje.delete(data)
   return redirect("/dashboard")

@app.route("/ver/<int:id>")
def ver_viaje(id):
    data={
        "id": id
    }
    viaje = Viaje.get_one(data)
    viajeros = Viajero.get_all(data)
    condicional = isViajero(viaje, viajeros)
    return render_template("viaje.html", viaje = viaje, viajeros = viajeros, condicional = condicional)

def isViajero(viaje:Viaje, viajeros:Viajero):
    if session['id_usuario'] == viaje.organizador_id  :
        return 'organizador'
    for row in viajeros:
        if session['id_usuario'] == row.usuario_id :
            return 'cancelar'
    return 'unirme'