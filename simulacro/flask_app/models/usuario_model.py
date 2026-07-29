# ==========================================
# example_model.py
# Modelo de ejemplo con conexión a MySQL
# ==========================================
from flask_app.config.mysqlconnection import connectToMySQL

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

    # Guardar un nuevo registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    # Login de usuario
    @classmethod
    def login(cls,data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s AND password = %(password)s"
        resultados = connectToMySQL(cls.DB).query_db(query,data)
        for usuario in resultados:
            return cls(usuario)

    # Obtener todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.DB).query_db(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))
        return usuarios
