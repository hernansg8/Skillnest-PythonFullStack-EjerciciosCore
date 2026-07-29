# ==========================================
# main_controller.py
# Controlador de ejemplo con rutas GET y POST
# ==========================================
# from flask_app.config.mysqlconnection import connectToMySQL  # Para consultas directas si se necesita

from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.usuario_model import Usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar/save', methods=['POST'])
def crear_usuario():
    #Validar password:
    if request.form['password'] != request.form['validpassword']:
        print("Error: las contraseñas no coinciden.")
        return redirect('/')
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    Usuario.save(data)
    return redirect('/')

@app.route('/iniciar/login', methods=['POST'])
def login_usuario():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    try:
        usuario = Usuario.login(data)
        session['id_usuario'] = usuario.id
        session['nombre_usuario'] = usuario.nombre
        return redirect('/dashboard')
    except ValueError:
        print('Error iniciando sesion')
        return redirect('/')

@app.route('/cerrarsesion')
def close_login():
    session.clear()
    return redirect('/')