from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.estudiante_model import Estudiante
from flask_app.models.curso_model import Curso

@app.route('/estudiante')
def estudiante():
    cursos = Curso.get_all()
    return render_template('estudiante.html', cursos = cursos)

@app.route('/estudiante/crear', methods=['POST'])
def crear_estudiante():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.save(data)
    return redirect('/cursos')