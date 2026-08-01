from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Evento:

    DB = "esquema_eventos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre_evento = data['nombre_evento']
        self.ubicacion = data['ubicacion']
        self.fecha = data['fecha']
        self.detalles = data['detalles']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Guardar un nuevo registro:
    @classmethod
    def save(cls, data):
        query = "INSERT INTO eventos" \
        " (nombre_evento, ubicacion, fecha, detalles, usuario_id, created_at, updated_at)" \
        " VALUES (%(nombre_evento)s, %(ubicacion)s, %(fecha)s, %(detalles)s, %(usuario_id)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM eventos JOIN usuarios ON usuarios.id = eventos.usuario_id ORDER BY eventos.fecha ASC;"
        results = connectToMySQL(cls.DB).query_db(query)
        items = []
        if results:
            for row in results:
                items.append(row)
        return items

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM eventos JOIN usuarios ON usuarios.id = eventos.usuario_id" \
                " WHERE eventos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        items = []
        if results:
            items = results[0]
        return items

    @classmethod
    def update(cls,data):
        query = "UPDATE eventos SET nombre_evento=%(nombre_evento)s, ubicacion=%(ubicacion)s, fecha=%(fecha)s, detalles=%(detalles)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM eventos WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @staticmethod
    def valid_data(data):
        valid = True
        if not data['nombre_evento']:
            flash('El campo Nombre no puede ir vacio.','error')
            valid = False
        if not data['ubicacion']:
            flash('El campo ubicacion no puede ir vacio.','error')
            valid = False
        if not data['fecha']:
            flash('El campo fecha no puede ir vacio.','error')
            valid = False
        if not data['detalles']:
            flash('El campo detalles no puede ir vacio.','error')
            valid = False
        return valid