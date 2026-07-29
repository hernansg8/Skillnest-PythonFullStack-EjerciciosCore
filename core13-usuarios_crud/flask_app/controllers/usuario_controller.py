from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.usuario_models import Usuario

@app.route("/usuarios")
def usuarios():
   usuarios = Usuario.get_all()
   print(usuarios)
   return render_template("usuarios_list.html", lista_usuarios = usuarios)

@app.route("/usuarios/nuevo")
def usuario_nuevo():
   return render_template("usuarios_form.html")

@app.route("/usuarios/save", methods=['POST'])
def usuario_save():
   datos = {
       "nombre": request.form['nombre'],
       "apellido": request.form['apellido'],
       "email": request.form['email']
   }
   Usuario.save(datos)
   return redirect("/usuarios")

@app.route("/usuarios/<int:id>")
def usuario_get(id):
   datos={
      "id": id
   }
   usuario = Usuario.get_one(datos)
   print(usuario)
   return render_template("usuario_data.html", user = usuario)

@app.route("/usuarios/borrar/<int:id>")
def usuario_delete(id):
   datos={
      "id": id
   }
   Usuario.delete(datos)
   return redirect("/usuarios")

@app.route("/usuarios/editar/<int:id>")
def usuario_editar(id):
   datos={
      "id": id
   }
   usuario = Usuario.get_one(datos)
   return render_template("usuario_update.html", user = usuario)

@app.route("/usuarios/update", methods=['POST'])
def usuario_update():
   datos = {
      "id":request.form['id'],
      "nombre": request.form['nombre'],
      "apellido": request.form['apellido'],
      "email": request.form['email']
   }
   Usuario.update(datos)
   return redirect("/usuarios")