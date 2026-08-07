from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario_model import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar/save', methods=['POST'])
def crear_usuario():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password'],
        "validpassword":request.form['validpassword']
    }
    #Validar formulario:
    if not Usuario.validar_form(data):
        return redirect('/')
    #Encriptar contraseña:
    pw_hashed = bcrypt.generate_password_hash(request.form['password'])
    data['password']=pw_hashed
    #Guardar:
    new_registro = Usuario.save(data)
    if new_registro > 0:
        flash('Usuario registrado correctamente.','register-success')
    else:
        flash('No se pudo registrar el usuario.','register-error')
    return redirect('/')

@app.route('/iniciar/login', methods=['POST'])
def login_usuario():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    #Comprobar que exista:
    usuario = Usuario.login(data)
    if not usuario:
        flash('Correo no registrado.','error')
        return redirect('/')
    #Comprobar password:
    if not bcrypt.check_password_hash(usuario.password,request.form['password']):
        flash('Contraseña incorrecta.','error')
        return redirect('/')
    #Sesión iniciada:
    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    session['usuario_apellido'] = usuario.apellido
    session['usuario_email'] = usuario.email
    return redirect('/dashboard')

@app.route('/cerrarsesion')
def close_login():
    session.clear()
    return redirect('/')