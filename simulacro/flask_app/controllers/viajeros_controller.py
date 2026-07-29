from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.viajeros_model import Viajero

@app.route('/viajero/save', methods=['POST'])
def guardar():
    data = {
        "viaje_id": request.form['viaje_id'],
        "usuario_id": request.form['usuario_id']
    }
    Viajero.save(data)
    return redirect(f'/ver/{request.form['viaje_id']}')

@app.route('/viajero/delete', methods=['POST'])
def eliminar():
    data = {
        "viaje_id": request.form['viaje_id'],
        "usuario_id": request.form['usuario_id']
    }
    Viajero.delete(data)
    return redirect(f'/ver/{request.form['viaje_id']}')