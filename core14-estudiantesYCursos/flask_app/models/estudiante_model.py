from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:

    DB = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM estudiantes WHERE curso_id = %(curso_id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        estudiantes = []
        for row in results:
            estudiantes.append(cls(row))
        return estudiantes
