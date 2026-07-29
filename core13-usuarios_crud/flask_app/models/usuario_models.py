# Importamos la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de usuarios
class Usuario:

    esquema = 'esquema_usuarios'

    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL(Usuario.esquema).query_db(query)

        array_usuarios = []
        for usuario in resultados:
            array_usuarios.append( cls(usuario) )
        return array_usuarios

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('esquema_usuarios').query_db(query, datos)

    @classmethod
    def get_one(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s ;"
        resultados = connectToMySQL('esquema_usuarios').query_db(query,datos)
        for usuario in resultados:
            return cls(usuario)

    @classmethod
    def delete(cls,datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('esquema_usuarios').query_db(query,datos)

    @classmethod
    def update(cls,datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL('esquema_usuarios').query_db(query,datos)
