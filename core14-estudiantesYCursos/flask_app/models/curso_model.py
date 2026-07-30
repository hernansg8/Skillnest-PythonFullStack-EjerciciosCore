from flask_app.config.mysqlconnection import connectToMySQL

class Curso:

    DB = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL(cls.DB).query_db(query)
        cursos = []
        for row in results:
            cursos.append(cls(row))
        return cursos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        curso = []
        for row in results:
            curso = cls(row)
        return curso

    @classmethod
    def get_estudiantes(cls,data):
        query = "SELECT cursos.id, cursos.nombre, estudiantes.nombre, estudiantes.apellido, estudiantes.edad" \
                " FROM cursos" \
                " JOIN estudiantes ON estudiantes.curso_id = cursos.id" \
                " WHERE cursos.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        estudiantes = []
        for row in results:
            estudiantes.append(row)
        return estudiantes