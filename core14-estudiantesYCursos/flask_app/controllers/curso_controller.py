from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.curso_model import Curso

@app.route('/cursos')
def index():
    cursos = Curso.get_all()
    return render_template('index.html', cursos = cursos)

@app.route('/cursos/crear', methods=['POST'])
def crear_curso():
    data = {
        "nombre": request.form['nombre']
    }
    Curso.save(data)
    return redirect('/cursos')

@app.route('/cursos/<int:id>')
def curso(id):
    data = {
        "id": id
    }
    curso = Curso.get_one(data)
    print(curso)
    estudiantes_curso = Curso.get_estudiantes(data)
    return render_template('curso.html', curso = curso, estudiantes = estudiantes_curso)
