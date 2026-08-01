from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.evento_model import Evento

@app.route('/eventos')
def home():
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        #Traemos todos los eventos vigentes:
        eventos = Evento.get_all()
        return render_template('eventos.html', eventos = eventos)

@app.route('/nuevo')
def nuevo():
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        return render_template('evento_nuevo.html')

@app.route('/ver/<int:id>')
def ver(id):
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        #Obtener datos del evento:
        evento = Evento.get_one({'id':id})
        print(evento)
        return render_template('evento_detalle.html', evento = evento)

@app.route('/editar/<int:id>')
def editar(id):
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        #Obtener datos del evento:
        evento = Evento.get_one({'id':id})
        return render_template('evento_editar.html', evento = evento)

@app.route('/eventos/borrar/<int:id>')
def borrar(id):
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        Evento.delete({'id':id})
        flash('El evento fué borrado con éxito.','success')
        return redirect('/eventos')

@app.route('/nuevo/save', methods=['POST'])
def crear_evento():
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        data = {
            "nombre_evento": request.form['nombre_evento'],
            "ubicacion": request.form['ubicacion'],
            "fecha": request.form['fecha'],
            "detalles": request.form['detalles'],
            "usuario_id": request.form['usuario_id']
        }
        #Validar formulario:
        if not Evento.valid_data(data):
            return redirect('/nuevo')
        #Guardar:
        new_registro = Evento.save(data)
        if new_registro > 0:
            flash('Evento guardado correctamente.','success')
            return redirect('/eventos')
        else:
            flash('El evento no se pudo guardar.','error')
            return redirect('/nuevo')

@app.route('/editar/save', methods=['POST'])
def editar_evento():
    #Comprobar inicio de sessión:
    if 'usuario_id' not in session:
        return redirect('/')
    else:
        data = {
            "id": request.form['id'],
            "nombre_evento": request.form['nombre_evento'],
            "ubicacion": request.form['ubicacion'],
            "fecha": request.form['fecha'],
            "detalles": request.form['detalles'],
            "usuario_id": request.form['usuario_id']
        }
        #Validar formulario:
        if not Evento.valid_data(data):
            return redirect(f'/editar/{request.form['id']}')
        #Guardar:
        Evento.update(data)
        return redirect('/eventos')
