from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Usuario:

    DB = "esquema_simulacro"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Guardar un nuevo registro:
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    # Login de usuario:
    @classmethod
    def login(cls,data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return False
        else:
            return (cls(results[0]))

    # Encontrar Email
    @classmethod
    def exist_email(cls,data):
        query = "SELECT email FROM usuarios WHERE email=%(email)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return False
        return True

    # Obtener todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.DB).query_db(query)
        items = []
        if results:
            for row in results:
                items.append(cls(row))
        return items

    #Validar los registros:
    @staticmethod
    def validar_form(data):
        patron_letras = re.compile(r'^[^\\W\\d_]+$')
        patron_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        valid = True
        if len(data['nombre'].strip())<2 or not patron_letras.match(data['nombre']):
            flash("El nombre debe ser solo letras y tener al menos 2 caracteres.","register-error") 
            valid = False
        if len(data['apellido'].strip())<2 or not patron_letras.match(data['apellido']):
            flash("El apellido debe ser solo letras y tener al menos 2 caracteres.","register-error") 
            valid = False
        if data['password'] != data['validpassword']:
            flash("Las contraseñas deben coincidir.","register-error")
            valid = False
        if not patron_email.match(data['email']):
            flash("El formato de correo no es válido.","register-error")
            valid = False
        if len(data['password'])<8:
            flash("La contraseña debe tener almenos 8 carácteres.","register-error")
            valid = False
        if Usuario.exist_email(data):
            flash("El correo ya se encuentra registrado.","register-error")
            valid = False
        return valid

