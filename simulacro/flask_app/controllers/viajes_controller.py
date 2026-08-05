from flask import render_template, redirect, request,session, flash
from flask_app import app
from flask_app.models.viajes_model import Viaje
from flask_app.models.viajeros_model import Viajero
from datetime import date

@app.route('/dashboard')
def dashboard():
    #Comprobar inicio de sessión:
    if 'usuario_id' in session:
        #Traemos todos los viajes vigentes:
        viajes = Viaje.get_all()
        return render_template('dashboard.html', viajes = viajes)
    else:
        return redirect('/')

@app.route('/nuevo')
def nuevo():
    #Comprobar inicio de sessión:
    if 'usuario_id' in session:
        return render_template('nuevo_viaje.html')
    else:
        return redirect('/')

@app.route('/nuevo/save', methods=['POST'])
def crear_viaje():
    data = {
        "destino": request.form['destino'],
        "fecha_inicio": request.form['fecha_inicio'],
        "fecha_fin": request.form['fecha_fin'],
        "itinerario": request.form['itinerario'],
        "organizador": request.form['organizador']
    }
    #Validar formulario:
    if not Viaje.validar_form(data):
        return redirect('/nuevo')
    #Guardar:
    new_registro = Viaje.save(data)
    if new_registro > 0:
        flash('Viaje guardado correctamente.','success')
    else:
        flash('El viaje no se pudo guardar.','error')
    return redirect('/dashboard')

@app.route('/editar/<int:id>')
def editar(id):
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        data={
            "id": id
        }
        #Obtener datos del viaje:
        viaje = Viaje.get_one(data)
        if viaje is None:
            return redirect('/dashboard')
        return render_template("editar_viaje.html", viaje = viaje)

@app.route('/editar/save', methods=['POST'])
def editar_viaje():
    data = {
        "id": request.form['id'],
        "destino": request.form['destino'],
        "fecha_inicio": request.form['fecha_inicio'],
        "fecha_fin": request.form['fecha_fin'],
        "itinerario": request.form['itinerario'],
        "organizador": request.form['organizador']
    }
    #Validar formulario:
    if not Viaje.validar_form(data):
        return redirect(f'/editar/{request.form['id']}')
    #Guardar:
    Viaje.update(data)
    flash('Viaje actualizado correctamente.','success')
    return redirect('/dashboard')

@app.route("/dashboard/borrar/<int:id>")
def usuario_delete(id):
   #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        data={
            "id": id
        }
        #Borrar registro:
        Viaje.delete(data)
        flash('El viaje fué borrado con éxito.','success')
        return redirect("/dashboard")

@app.route("/ver/<int:id>")
def ver_viaje(id):
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        data={
            "id": id
        }
        #Obtener datos del viaje
        viaje = Viaje.get_one(data)
        if viaje is None:
            return redirect('/dashboard')
        #Obtener viajeros que se han unido:
        viajeros = Viajero.get_all(data)
        #Condicional para saber si puede puede o nó unirse:
        condicional = isViajero(viaje, viajeros)
        #Renderizar:
        return render_template("viaje.html", viaje = viaje, viajeros = viajeros, condicional = condicional)

def isViajero(viaje:Viaje, viajeros:Viajero):
    if session['usuario_id'] == viaje.organizador_id  :
        return 'organizador'
    for row in viajeros:
        if session['usuario_id'] == row.usuario_id :
            return 'cancelar'
    return 'unirme'